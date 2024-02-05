import glob
import json
import os
from typing import List
#import logging
#from datetime import datetime

import psycopg2

# Set up logging
#logging.basicConfig(level=logging.WARNING)

def get_files(filepath: str) -> List[str]:
    """
    Description: This function is responsible for listing the files in a directory
    """

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print(f"{num_files} files found in {filepath}")

    return all_files


def process(cur, conn, filepath):
    # Get list of files from filepath
    all_files = get_files(filepath)

    # get datetime
    #curr_dt = datetime.now()

    for datafile in all_files:
        with open(datafile, "r") as f:
            data = json.loads(f.read())
            for each in data:
                # Print some sample data
                
                if each["type"] == "IssueCommentEvent":
                    print(
                        each["id"], 
                        each["type"],
                        each["actor"]["id"],
                        each["actor"]["login"],
                        each["actor"]["display_login"],
                        each["actor"]["gravatar_id"],
                        each["actor"]["url"],
                        each["actor"]["avatar_url"],
                        each["repo"]["id"],
                        each["repo"]["name"],
                        each["created_at"],
                        each["payload"]["issue"]["url"],
                    )
                else:
                    print(
                        each["id"], 
                        each["type"],
                        each["actor"]["id"],
                        each["actor"]["login"],
                        each["actor"]["display_login"],
                        each["actor"]["gravatar_id"],
                        each["actor"]["url"],
                        each["actor"]["avatar_url"],
                        each["repo"]["id"],
                        each["repo"]["name"],
                        each["created_at"],
                    )

                # Insert data into tables here
                insert_statement = f"""
                    INSERT INTO actors (
                        actor_id, 
                        actor_login, 
                        actor_display_login, 
                        actor_gravatar_id, 
                        actor_url, 
                        actor_avatar_url
                ) VALUES (  '{each["actor"]["id"]}', 
                            '{each["actor"]["login"]}',
                            '{each["actor"]["display_login"]}',
                            '{each["actor"]["gravatar_id"]}',
                            '{each["actor"]["url"]}',
                            '{each["actor"]["avatar_url"]}')
                    ON CONFLICT (actor_id) DO NOTHING
                """
                # print(insert_statement)
                cur.execute(insert_statement)

                # Insert data into tables here
                # insert_statement = f"""
                #     INSERT INTO events (
                #         id,
                #         type,
                #         actor_id
                #     ) VALUES ('{each["id"]}', '{each["type"]}', '{each["actor"]["id"]}')
                #     ON CONFLICT (id) DO NOTHING
                # """
                # # print(insert_statement)
                # cur.execute(insert_statement)

                conn.commit()


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )
    #logging.warning('connected postgresdb')
    cur = conn.cursor()

    process(cur, conn, filepath="../data")
    #logging.warning('wrote to db')

    conn.close()
    #logging.warning('disconnect postgresdb--closed')


if __name__ == "__main__":
    main()
# 1.Data Modeling with PostgreSQL

### Get Start
-------------

'$ pip install psycopg2'

docker nginx
'$docker run -p 8080:80 nginx'

* __Port__  8080 = Adminer
            5432 = Postgres

### Running Postgres
-------------
'$ docker compose up

Connect postgres and login: http://localhost:8080/
* System: PostgreSQL
* Server: postgres
* Username: postgres
* Password: postgres
* Database: postgres

### Insert your 'code' here 

create table:
'$ python create_tables.py' 

insert data into tables:
'$ python etl.py' 

To shutdown, press Ctrl+C and run (close webserver): 
'$ docker compose down'
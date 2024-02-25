# Building a Data Warehouse with BigQuery (GCP)

## Started
### Getting Started
```sh
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

### Running ETL Script
```sh
python etl.py
```

### Set def main(dataset_id, table_id, file_path)
```sh
main(dataset_id="github", table_id="events", file_path="github_events.csv")
```

![def main](https://github.com/Yanadade/Data-Warehouse-Business-Intel/blob/main/4-Data%20Warehouse-Bigquery/Image/1.def%20main.JPG)


### Set Project ID
```sh
project_ID = ""YOUR_GCP_PROJECT""
```


### Set Keyfile Path
```sh
keyfile = ""YOUR_KEYFILE_PATH""
```

### Keyfile Path in GCP
```sh
IAM & Admin --> Service Accounts
Create Service Accounts : 
    Service accounts details: Service account name
    Grant account access to project: Role
    Grant user access to service account: Done
    Create private key type: JSON
```

![Keyfile Path](https://github.com/Yanadade/Data-Warehouse-Business-Intel/blob/main/4-Data%20Warehouse-Bigquery/Image/2.Keyfile%20path.JPG)


### Load data to BigQuery
```sh
python etl.py
```
![BigQuery](https://github.com/Yanadade/Data-Warehouse-Business-Intel/blob/main/4-Data%20Warehouse-Bigquery/Image/3.python%20etl.JPG)


### Add Actor in etl and show in bigquery
```sh
Delete events
python etl.py
Create new events
```

![Actor in etl0](https://github.com/Yanadade/Data-Warehouse-Business-Intel/blob/main/4-Data%20Warehouse-Bigquery/Image/4.python%20etl%20%20add%20actor%201.JPG)

![Actor in etl1](https://github.com/Yanadade/Data-Warehouse-Business-Intel/blob/main/4-Data%20Warehouse-Bigquery/Image/5.python%20etl%20%20add%20actor%202.JPG)


![Actor in BigQuery](https://github.com/Yanadade/Data-Warehouse-Business-Intel/blob/main/4-Data%20Warehouse-Bigquery/Image/6.python%20etl%20%20add%20actor%203.JPG)


### Query Data

![Query Data](https://github.com/Yanadade/Data-Warehouse-Business-Intel/blob/main/4-Data%20Warehouse-Bigquery/Image/7.query.JPG)
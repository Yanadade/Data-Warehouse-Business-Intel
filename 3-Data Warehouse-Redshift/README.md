# Building a Data Warehouse

## Getting Started

### 1. Create AWS S3
* go to aws console - S3 
* create bucket
  - make sure - [x] **Block all public access** 
  - keep - [x] Disable for Bucket Versioning
  - create bucket
### upload json to bucket
* Json event file
* Json path file

![AWS S3](https://github.com/Yanadade/Data-Warehouse-Business-Intel/blob/main/3-Data%20Warehouse-Redshift/Image/S3.JPG)

### Check IAM Role for LabRole
* go IAM
* choose Role
* seach "LabRole"
* copy ARN

### 2. Create cluster AWS Redshift and enable public
* go to aws console - Redshift 
* Provision (create) cluster

- AQUA (Advanced Query Accelerator) turn off
- Node type = ra3.xplus  - the smallest
- Number of node = 1
  - awsuser
  - set password
- click Associate IAM roles select 
   - [x] LabRole and click Associate IAM roles
- Additional configurations deselect 
   - [ ] Use defaults
- Network and security
  - Default VPC
  - VPC security groups use default
  - Cluster subnet group use Cluster subnet group-1 (it don't have create one in Configuration > subnet group , with all available zone)
  - leave the remaining default
  - create cluster

![AWS Redshift](https://github.com/Yanadade/Data-Warehouse-Business-Intel/blob/main/3-Data%20Warehouse-Redshift/Image/redshift.JPG)

### 3. S3 Connection path
![S3 Connection path](https://github.com/Yanadade/Data-Warehouse-Business-Intel/blob/main/3-Data%20Warehouse-Redshift/Image/S3%20connect%20path.JPG)

### 4. Redshift Connection path
![Redshift Connection path](https://github.com/Yanadade/Data-Warehouse-Business-Intel/blob/main/3-Data%20Warehouse-Redshift/Image/Redshift%20connect%20path.JPG)

## create table in Redshift

```sh
CREATE TABLE IF NOT EXISTS github_event (
  event_id text primary key,
  event_type text,
  actor_login text,
  repo_name text,
  created_at text
  
)
```

## insert data from json with json_path

```sh
copy github_event
from 's3://dw-yana/github_events_01.json'
iam_role 'arn:aws:iam::905418110941:role/LabRole' 
json 's3://dw-yana/events_json_path.json';
```

To show data in table public:

```sh
select
    eventname, 
    avg(commission) 
from 
    sales
join event on sales.eventid = event.eventid
group by eventname
```
![Redshift Query](https://github.com/Yanadade/Data-Warehouse-Business-Intel/blob/main/3-Data%20Warehouse-Redshift/Image/redshift_query.JPG)

To close all service
- S3 empty bucket
- Delete S3 bucket
- Delete Redshift cluster** with out keeping snapshot** - [ ] snap shot 

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
# Building a Data Warehouse

## Getting Started
### create cluster AWS Redshift
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

### create bucket AWS S3
* go to aws console - S3 
* create bucket
  - make sure - [x] **Block all public access** 
  - keep - [x] Disable for Bucket Versioning
  - create bucket
### upload json to bucket
* Json event file
* Json path file

### Check IAM Role for LabRole
* go IAM
* choose Role
* seach "LabRole"
* copy ARN

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
![AWS Redshift query console](xxx)

## insert data from json with json_path

```sh
copy github_event
from 'xxx'
iam_role 'xxx' 
json 'xxx';
```

To show data in table github_event:

```sh
select * from github_event
```
see the result in 
[github_event_query_result.csv](xxx)

example result
| event_id	  |   event_type      |actor_login  |	repo_name	                    | created_at           |
| :---        |   :---            |:---:        |:---:                          | ---:                 |
|23487929637  |	IssueCommentEvent	|  xx	  |xx	            | xx |
|23487929676	|PushEvent	        |  xx	  |xx	          | xx |
|23487929674	|PushEvent	        |  xx	  |xx        |	xx |
|23487929661	|PushEvent	        |  xx	|xx |xx  |

To close all service
- S3 empty bucket
- Delete S3 bucket
- Delete Redshift cluster** with out keeping snapshot** - [ ] snap shot 


## watch cost explorer

![cost](xxx)


![AWS Redshift query console](xxx)

## Data Model
![data model](xxx)

### 1. Create AWS S3
![AWS S3]()

### 2. Create AWS Redshift and enable public
![AWS Redshift](xxx)

### 3. S3 Connection path
![S3 Connection path](xxx)

### 4. Redshift Connection path
![Redshift Connection path](xxx)


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
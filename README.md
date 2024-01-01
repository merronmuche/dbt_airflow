


# Data warehouse tech stack with Postgresql, DBT, Airflow

## Introduction

our colleagues have joined to create an AI startup that deploys sensors to businesses, collects data from all 
activities in a business - people’s interaction, traffic flows, smart appliances installed in a company.
ourstartup helps organisations obtain critical intelligence based on public and private data they collect
 and organise. 

## Objective
Our objective is to reduce the cost of running the client facility as well as to increase
the livability and productivity of workers by creating a scalable data warehouse
tech-stack that will help us provide the AI service to the client.


## Challenges
    Since I'm not familiar with the terms mentioned, combining Airflow, dbt, and Redash turned out to be tough because it needed a lot of time and resources. Setting up and connecting these different tools required careful planning of settings and connections, making the integration process more complicated.

    Understanding the dataset posed a challenge as it lacked detailed descriptions for effective data manipulation and transformation. and the project faced issues due to the dataset's lack of clarity. Additionally, when running Redash, the creation of multiple containers significantly slowed down my PC, eventually causing it to stack up numerous times.


## Screenshots:

[schedule](https://drive.google.com/file/d/1LZ_LVsXeaay3d5xPiec-EeuRVa2vdkf0/view?usp=sharing)
[dbt](https://drive.google.com/file/d/18nZ9B6Ndf8Yhy5IuCJAvQz7GqTq_Leyr/view?usp=sharing)

## Documentation:

clone the project 
```
git clone https://github.com/merronmuche/dbt_airflow
```
then create a virtual environment
```virtualenv venv
source venv/bin/activate
```
then run the requirements

```
pip install -r requirements.txt

run docker compose 
```
docker compose up

## Steps for dbt:

 Set up a dbt project using `dbt init`.
 Configure database connection in `profiles.yml`.
 Define models in the `models` directory.
 Run dbt models using `dbt run`.
 Generate documentation with `dbt docs generate`.
 Share documentation on [dbt Cloud](https://cloud.getdbt.com/).
 Capture a screenshot of the data view and place it in the "screenshots" folder.

 ## References
 'https://docs.getdbt.com/docs/collaborate/documentation'
 'https://airflow.apache.org/docs/'


# How to run the app
## run airflow

First create user using the following command

```bash
airflow users create \
    --username [your_username] \
    --firstname [Your First Name] \
    --lastname [Your Last Name] \
    --role Admin \
    --email [your-email@example.com] \
    --password [your_password]
```

Then, run the following command
```bash
airflow db init```

Then, go to localhost:8080 and login with the above credentials.



##  Redash

### Step 1: Create a `.env` File
- Copy the `.env.sample` file.
- Modify the values in the copied file to suit your local environment.
- Save it as `.env`.

### Step 2: Create the Database
Run the following command to create the database:
\```bash
docker-compose run --rm redash-server create_db
\```

### Step 3: Build and Run Docker Compose
Build and run the Redash services using the following command:
\```bash
docker-compose up --build
\```

### Step 4: Access Redash
- Open your web browser.
- Navigate to `localhost:5000`.

### Reference
For more detailed configuration, refer to the official Redash Docker Compose file:
[Redash Docker Compose File on GitHub](https://github.com/getredash/setup/blob/master/data/docker-compose.yml)



# Load Test Application

## Running The Application
The application is a dummy api to test combinations of using Faker to create generative data for your load test. You could introduce characters not excepted by your request specifications, strings that are too long for certain fields, etc. by customizing the Lorem Provider.

[Read more about Faker](https://pypi.org/project/Faker/)

### Run Locally

#### Steps
- Navigate to the downloaded repo and run the following command
`python3 app.py`

### Run With Docker
This repo includes a dockerfile with all the dependencies

#### Steps
- Navigate to the directory of the dockerfile and enter the following commands in the terminal
`sudo docker build -t loadtestproject .`
`sudo docker run -ti -p 5000:5000 loadtestproject bash`
- Inside the bash, run the following command
`python3 app.py`

#### Developing on Mac (Requirements)
In order to develop for the DB version of the app, you must use install the flask_mysqldb. In order to install this module you will need mysql and mysqlclient installed. You can install both using Homebrew

### Run DB Version With Docker
For DB version, follow the same steps as listed above with docker but within the DB_APP folder. You will run the command `python3 app_db.py` instead of `python3 app.py'

#### Steps
Run the following commands:
- `docker build -t admin1/mysql01 .`
- `docker run --name author_quotes2 -p3306 -d admin1/mysql01`
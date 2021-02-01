# **Tutorial Run PostgresSQL, PGAdmin, & FastAPI in Docker Container**

1. Prepare `docker-compose.yml` file and create network:
```docker
version: "3.8"

services: 
  db:
    image: timescale/timescaledb:2.0.0-pg12
    ports: 
      - "5432:5432"
    environment: 
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=savtrik

  backend:
    build: .
    volumes:
      - .:/app
    command: bash -c "uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
    ports: 
      - "8000:8000"
    depends_on: 
      - db

  pg-admin:
    image: dpage/pgadmin4:latest
    environment: 
      PGADMIN_DEFAULT_EMAIL: "admin@savtrik.com"
      PGADMIN_DEFAULT_PASSWORD: "savtrik123"
    ports: 
      - "5050:80"
    depends_on:
      - db
```
2. Build docker image using `docker-compose build` and then run docker containers using `docker-compose up`.
3. To make sure the program running, then go to `pgAdmin` and create new server using the `PostgreSQL User` & `PostgreSQL Password`. Before that, login `pgAdmin` using this account:
```
PGADMIN_DEFAULT_EMAIL: admin@savtrik.com
PGADMIN_DEFAULT_PASSWORD: savtrik123
```
Then create new server with this data
```
(General)
Name : savtrikdb

(Connection)
Host        : 172.20.0.2     #IPAdress savtrik network (by inspect the db container network)
Port        : 5432           #internal port (docker container)
db name     : savtrik
Username    : postgres
Password    : postgres
```
4. Now open `postgresql` shell cli (bash) by go to docker CLI and create a table in your `savtrik` database
```
> bash 
> psql postgres://postgres:postgres@localhost:5432/savtrik
> CREATE TABLE IF NOT EXISTS numbers (number BIGINT, timestamp BIGINT);
> \dt  # Show the existing tables 
```
5. Now create `python` file (ex. `hello.py`) and use this command to copy the python file into docker container directory
```
> docker cp hello.py 11625c52e112:/.  # docker cp [current file/dir] [container id]:[destination dir]
``` 
and go to `python` docker cli and try to run the program using this command
```
> python hello.py
Hello!!!
```
If it's works, then create another python program to try postgres db connection.
```python
import time
import random

from sqlalchemy import create_engine

db_name = 'savtrik'
db_user = 'postgres'
db_pass = 'postgres'
db_host = 'localhost'
db_port = '5432'

# Connecto to the database
db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

def add_new_row(n):
    # Insert a new number into the 'numbers' table.
    db.execute("INSERT INTO numbers (number,timestamp) "+ "VALUES ("+ str(n) + "," + str(int(round(time.time() * 1000))) + ");")

def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = "" + "SELECT number " + "FROM numbers " + "WHERE timestamp >= (SELECT max(timestamp) FROM numbers)" + "LIMIT 1"

    result_set = db.execute(query)  
    for (r) in result_set:  
        return r[0]

if __name__ == '__main__':
    print('Application started')

    while True:
        add_new_row(random.randint(1,100000))
        print('The last value insterted is: {}'.format(get_last_row()))
        time.sleep(5)
```
Then run it, need to remember, if you use in local, set the `db_host = localhost`, then if you run it using docker container cli, then set the `db_host = 172.20.0.2` *(it may be different IPAdress, depend on the running docker network at that time)*

**Running Docker Containers**
```
> docker ps
CONTAINER ID   IMAGE                              COMMAND                  CREATED       STATUS       PORTS                           NAMES
11625c52e112   production_backend                 "bash -c 'uvicorn ma…"   2 hours ago   Up 2 hours   0.0.0.0:8000->8000/tcp          production_backend_1
4250dc15d02e   dpage/pgadmin4:latest              "/entrypoint.sh"         2 hours ago   Up 2 hours   443/tcp, 0.0.0.0:5050->80/tcp   production_pg-admin_1
c6579cfe93fd   timescale/timescaledb:2.0.0-pg12   "docker-entrypoint.s…"   2 hours ago   Up 2 hours   0.0.0.0:5432->5432/tcp          production_db_1
```

**Docker Images**
```
> docker images
REPOSITORY              TAG          IMAGE ID       CREATED       SIZE
production_backend      latest       8e5d729601ae   2 hours ago   979MB
python                  3.7          ca194d6afe58   9 days ago    876MB
timescale/timescaledb   2.0.0-pg12   9a94ba119602   2 weeks ago   185MB
dpage/pgadmin4          latest       b848a8a52bff   6 weeks ago   227MB
```

**If you get an error with your running container**, then stop and doing a full blown reset on your environment by running `docker-compose down -v`

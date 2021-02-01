# **How to run TimescaleDB + PostgreSQL + PGAdmin in Docker**

Link Tutorial: [PGAdmin and PostgreSQL with Docker-compose.yml](https://www.youtube.com/watch?v=XeLg525z-eE)

1. First you need to create the `docker-compose.yml` file:
```docker
version: "3"
services:
  demo-container-db:
    image: timescale/timescaledb:2.0.0-pg12
    environment:
      POSTGRES_USER: savtrik
      POSTGRES_PASSWORD: 2345678910Aa
    ports:
    - "5432:5432"
    networks:
    - savtrik_network
    volumes:
    - db-data:/var/lib/postgresql/data
  demo-pgadmin4:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: savtrik@gmail.com
      PGADMIN_DEFAULT_PASSWORD: password
    ports:
    - "8888:80"
    networks:
    - savtrik_network
    
networks:
  savtrik_network:
    driver: bridge
  
volumes:
  db-data:
```
2. then run the `docker-compose` file using command below:
```
> docker-compose up
```
3. Now acces the `PGAdmin` using port `localhost:8888` and login using the following defined account:
```
PGADMIN_DEFAULT_EMAIL: savtrik@gmail.com
PGADMIN_DEFAULT_PASSWORD: password
```
4. Then connect to postgres database by connecting to the `server`, and type the following input:
```
(General)
Name : Savtrik Server

(Connection)
Host        : localhost     #localhost
Port        : 5432          #external port
Username    : savtrik
Password    : 2345678910Aa
```
It will unable to connect (because both of PGAdmin and postgres work in bridge network inside docker). So, you need to use the internet port in docker network, by go to `CMD` and type:
``` 
> docker container ls
> docker inspect 284568440c19   #container ID

                    "Links": null,
                    "Aliases": [
                        "284568440c19",
                        "demo-container-db"
                    ],
                    "NetworkID": "d2c6b488c1d4a0e932acf1a433379820a386d7f46e42d72fccf595ac767a5175",
                    "EndpointID": "9498cf55b36b2c4d1e1a0a7d897873e608e20ce854ba7ac873d109fb04963b1b",
                    "Gateway": "172.18.0.1",
                    "IPAddress": "172.18.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:12:00:02",
                    "DriverOpts": null
```
And get the `IPAdress` inside the docker inspect : `172.18.0.2`. And go back to pgadmin and input the following data:
```
(General)
Name : Savtrik Server

(Connection)
Host        : 172.18.0.2     #IPAdress savtrik network
Port        : 5432           #internal port (docker)
Username    : savtrik
Password    : 2345678910Aa
```
5. If you going to connect databse externally, you can use the `external port:internal port` == `5432:5432`.
```
localhost:5432  #docker external port
```
or in `python`
```python
import urllib
import os

host_server = os.environ.get('host_server', 'localhost')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port','5432')))
database_name = os.environ.get('database_name', 'Savtrik Server')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username','savtrik')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password','2345678910Aa')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))

DATABASE_URL = "postgresql://{}:{}@{}:{}/{}?sslmode={}".format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
#DATABASE_URL = "sqlite:///./test.db"
```

##### Or, if you're going to use CLI docker command, you can run the psql shell
```
> psql -U postgres  # -U (User) 
``` 
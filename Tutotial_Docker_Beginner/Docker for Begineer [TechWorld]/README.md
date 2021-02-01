# **Docker Tutorial for Begineers [TechWorld]**

Link Youtube: [Docker for Begineers: Full Free Course!](https://www.youtube.com/watch?v=3c-iBn73dDE)

### **Developing with Docker Containers**
In here we need 3 different images to run the app, there are:
1. my-app:1.0 image
2. mongodb image
3. mongodb-express image

First, you need to pull mongodb image into your local.
```
> docker pull mongo
> docker pull mongo-express
```

Then, create `mongo-network`
```
> docker network create mongo-network
> docker network ls
```

Run the `mongodb` container in host:container ports, and in the environment variable you can set the `root username` and `root password`.  
```
> docker run -d \
>   -p 27017:27017 \ 
>   -e MONGO_INITDB_ROOT_USERNAME=admin \
>   -e MONGO_INITDB_ROOT_PASSWORD=password \ 
>   --name mongodb \
>   --network mongo-network \
>   mongo 
```
Then run the `mongo express`
```
> docker run -d \
>   -p 8081:8081 \
>   -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
>   -e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
>   --net mongo-network \
>   --name mongo-express \
>   -e ME_CONFIG_MONGODB_SERVER=mongodb \
>   mongo-expres
``` 
Let's see the mongo express logs & check the container mongo express in the browser `localhost:8081` and then create a database name `user-account`.
```
> docker logs [mongo-express container id]
> docker ps
```
Then connect the `node-js` to the `mongodb` database use the uri and the port. And specify the mongodb `username` and `password`. You need also declare the table name `users` in database `user-account`.
```javascript

var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://admin:password@localhost:27017', function(err, client){
    var db = client.db('user-account');
    db.collection('users').updateOne(query, newValue, {upsert: true}, function (err, res) {...})
});
```
Because the `mongodb` & `mongo-express` containers already running, then you can use the web app to get & update the input data. Then you can check the docker logs
```
> docker logs [mongodb container id]
> docker logs [mongodb container id] | tail
> docker logs [mongodb container id] -f
```

### **Docker Compose - Running Multiple Services**
Convert the `docker run command` into `mongo-docker-compose.yaml`
**docker run command**
```
> docker run -d \
>   -p 27017:27017 \ 
>   -e MONGO_INITDB_ROOT_USERNAME=admin \
>   -e MONGO_INITDB_ROOT_PASSWORD=password \ 
>   --name mongodb \
>   --network mongo-network \
>   mongo 

> docker run -d \
>   -p 8081:8081 \
>   -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
>   -e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
>   --net mongo-network \
>   --name mongo-express \
>   -e ME_CONFIG_MONGODB_SERVER=mongodb \
>   mongo-expres
```
**mongo-docker-compose.yaml**
```
version: '3'
service: 
    mongodb:                    #container name
        image: mongo            #image name
        ports:
            - 27017:27017       #host_port:container_port
        environment:
            - MONGO_INITDB_ROOT_USERNAME=admin
            - MONGO_INITDB_ROOT_PASSWORD=password
    mongo-express:
        image: mongo-express    
        ports:
            - 8080:8081
        environment:
            - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
            - ME_CONFIG_MONGODB_ADMINPASSWORD=password
            - ME_CONFIG_MONGODB_SERVER=mongodb
```
*Docker Compose takes care of creating a common Network!* 

Then save the docker compose int the repository code (part of the application code). To run the `docker container`, then use docker-compose
```
# Will start all of mongo containers in mongo.yaml
> docker-compose -f mongo.yaml up
# It will automatically create a default network as "myapp_default" with default driver
> docker network ls
```
To stop the running both containers, then you can type
```
> docker-compose -f mongo.yaml down
# and the default docker network will gone
```

### **Dockerfile-Building our own Docker Image**

If you going to create docker image from your app file, then you need to copy the artifact (jar, war, bundle.js) and create it in dockerfile.

**What is dockerfile?**
Dockerfile is the blueprint for docker images. So, the first line every dockerfile is `FROM [image]`

**Image Environment Blueprint**
```
install node:13-alpine

set MONGO_DB_USERNAME=admin
set MONGO_DB_PWD=password

create /home/app folder

copy current folder files to /home/app

start the app with: "node server.js"
```
**Dockerfile**
```
FROM node:13-alpine

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=password 

RUN mkdir -p /home/app

COPY . /home/app                        #source & target

CMD ["node", "/home/app/server.js"]     #after copy into /home/app directory
```
To build an image using dockerfile, we have to provide 2 parameters
```
> docker -t my-app:1.0 .    #location in current directory of my-app code
> docker images
> docker run my-app:1.0
```  
*When you adjust the Dockerfile, you must rebuild the Image!*
```
> docker rm [container id]
> docker rmi my-app:1.0
> docker -t my-app:1.0 .
> docker run my-app:1.0
```
The javascript container now running in your machine 

If you going to inspect the environment set then you can run `docker exec` 
```
> dokcer logs [container id]
> docker exec -t [container id] /bin/sh
> ls
> env

MONGO_DB_USERNAME=admin 
MONGO_DB_PWD=password
```

You can also check the another COPY directory
```
> ls /home/app
```

### **Private Docker Registry**
First step to create private repository for docker images. 
1. Go to aws.amazon.com. 
2. And service that going to use is **ECR (Elastic Container Registry)**.
3. Create repository and name it `my-app` (1 repository only for 1 images, but you can add more than 1 version)
4. Click the tick icon or the repository there and click the `view push commands` button, and follow the instruction
5. Go to terminal and type to login and authentication
```
# Retrieve the login command to use to authenticate your docker client to your registry.
> (aws ecr get-login --no-include-email --region eu-central-1)

# Build your docker image using the following command. 
> docker built -t my-app

# After the build completes, tag your image so you can push the image to this repository:
> docker tag my-app:1.0 664574038682.dkr.ecr.eu-central-1.amazonaws.com/my-app:1.0

# Run the following command to push this image to your newly created AWS repository:
> docker push 664574038682.dkr.ecr.eu-central-1.amazonaws.com/my-app:1.0
```
*Pre-Requisites:*
*1. AWS Cli needs to be installed*
*2. Credentials configured*

### **Deploy Our Contianerized App**
In here you will pull your my-app images from AWS repository and mongodb and mongo-express from docker hub. And in the end you need to deploy it into server. To do that, you need to integrate the my-app images into docker-compose.
```
version: '3'
service: 
    my-app:
        image: 664574038682.dkr.ecr.eu-central-1.amazonaws.com/my-app:1.0 
        ports:
            - 3000:3000
    mongodb:                    #container name
        image: mongo            #image name
        ports:
            - 27017:27017       #host_port:container_port
        environment:
            - MONGO_INITDB_ROOT_USERNAME=admin
            - MONGO_INITDB_ROOT_PASSWORD=password
    mongo-express:
        image: mongo-express    
        ports:
            - 8080:8081
        environment:
            - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
            - ME_CONFIG_MONGODB_ADMINPASSWORD=password
            - ME_CONFIG_MONGODB_SERVER=mongodb
```
*Note: the server needs to login to pull from AWS Private repository!*

To deploy your images, you need to `login` to AWS Repository
```
> docker login ...
```
then you need to create `mongo.yaml` file in the current dirrecotory
```
> vim mongo.yaml
[copy all docker-compose command into mongo.yaml file]
```
Then you can run the mongo.yaml file 
```
> docker-compose -f mongo.yaml up
```

and change the link in the `javascript` code to connect `nodejs` to `mongodb` server
```javascript
MongoClient.connect("mongodb://admin:password@localhost:27017")
// mongo db = name of the container or of the service that we specify here, 
// and you don't need to specify the host port because docker already set it for you 
MongoClient.connect("mongodb://admin:password@mongodb")
```
### **Docker Volumes - Persist data in Docker**
Current data which running in the container will be saved in `/var/lib/mysql/data` inside the container. If we going to restart the container, the data will gone.

So, you need data volume which plug the host file system with virtual file system (docker container). And the file location for host file system directory is `/home/mount/data`

You can create docker volumes using 3 methods: 
1. docker run command 
Host Volumes: you decide *where on the host file system* the reference is made
```
> -v /home/mount/data:/var/lib/mysql/data
```
2. docker run command 
Anonymous Volumes: for *each container a folder is generated* that gets mounted
```
> -v /var/lib/mysql/data
# Automatically create a dir by docker
# /var/lib/docker/volumes/random-hash/_data
```
3. docker run command
Named Volumes: you can reference the volume by name. This method should be used in production
```
> -v [name]:/var/lib/mysql/data
# Automatically create a dir by docker
# /var/lib/docker/volumes/random-hash/_data
```

For example:
```
version: '3'
service: 
    mongodb:                    #container name
        image: mongo            #image name
        ports:
            - 27017:27017 
        volumes:
            - db-data:/var/lib/mysql/data
volumes:
    db-data
```

### **Volumes Demo - Configure Persistence for our demo project**
```
version: '3'
service: 
    # my-app:
    #    image: 664574038682.dkr.ecr.eu-central-1.amazonaws.com/my-app:1.0 
    #    ports:
    #        - 3000:3000
    mongodb:                    #container name
        image: mongo            #image name
        ports:
            - 27017:27017       #host_port:container_port
        environment:
            - MONGO_INITDB_ROOT_USERNAME=admin
            - MONGO_INITDB_ROOT_PASSWORD=password
        volumes:
            - mongo-data:/data/db   #default data store in container directory
    mongo-express:
        image: mongo-express    
        ports:
            - 8080:8081
        environment:
            - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
            - ME_CONFIG_MONGODB_ADMINPASSWORD=password
            - ME_CONFIG_MONGODB_SERVER=mongodb
volumes:
    mongo-data:
        driver: local
```

where the docker volumes are located?

Windows: `C:\ProgramData\docker\volumes`
Linux: `/var/lib/docker/volumes`
Mac: `/var/lib/docker/volumes`
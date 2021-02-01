# **Docker for Begineers**

Link Youtube: [Docker for Begineers: Full Free Course!](https://www.youtube.com/watch?v=zJ6WbK9zFpI)

**Objectives:**
- What are Containers?
- What is Docker?
- Why do you need it?
- What can it do?
- Run Docker Containers
- Create a Docker Image
- Networks in Docker
- Docker Compose
- Docker Concepts in Depth
- Docker for Windows/Mac
- Docer Swarm
- Docker Kubernetes
- Conclusion
-----------------------------
## **DOCKER OVERVIEW**
### **1. What are Containers?**
### **2. What is Docker?**
### **3. Why do you need it?**
- Compatibility/Dependency
- Long Setup Time
- Different Dev/Test/Prod Environments
### **4. What Can it do?**
With docker I was able to run each
- Containerize Applications
- Run each Service with its own dependencies in separate containers.

**Container** is completely isolated environment, that they can have their own processes for services their own network interfaces their own mounts just like washing machines except they all share the same OS kernel. 

*Note:* If you run a container based on Linux and go see it's possible, it's means the well when you install docker on windows and run linux container on windows, you're not really running a Linux container on Windows, Windows runs a Linux Container on a Linux Virtual Machine under the hoods, so it's really Linux Container on Linux Virtual Machine on Windows. 

**Images:** Package or template just like VM template that you might worked with in the virtualization world it is used to create one or more containers. 

**Containers:** are running instances of images that are isolated and have their own environments and set of processors as we've seen before a lot of products have been docker iced already in case you can't find what you're looking for you can create your own image and push it to docker hub repository making it available for public, so if you look at it traditionally developers develop applications then they hand it over to ops team to deploy and manage it in production environments. they do that by providing a set of instructions such as information about how the hosts must be setup what prequisites are to be installed on the host and how the dependencies are to be configured etc, since the ops op

## **DOCKER INSTALLATION**
Go to docker website and follow the instruction.
To check the docker installed or not, type this command in your CMD:
```
> docker version
```
Then go to http://hub.docker.com, and you will find the most popular docker image, and you can search any fun docker images there. 

### **5. Run Docker Containers**
## **DOCKER COMMANDS**
If you going to pull docker images from docker hub, just go to docker hub and type the following command in windows terminal:
```
(ex.linux) > sudo docker run docker/whalesay cowsay Hello-World!

(format)   > docker pull [OPTIONS] NAME[:TAG|@DIGEST]

(example1) > docker pull debian
    Using default tag: latest
    latest: Pulling from library/debian
    fdd5d7827f33: Pull complete
    a3ed95caeb02: Pull complete
    Digest: sha256:e7d38b3517548a1c71e41bffe9c8ae6d6d29546ce46bf62159837aad072c90aa
    Status: Downloaded newer image for debian:latest

(example2) > docker pull debian:jessie
    jessie: Pulling from library/debian
    fdd5d7827f33: Already exists
    a3ed95caeb02: Already exists
    Digest: sha256:a9c958be96d7d40df920e7041608f2f017af81800ca5ad23e327bc402626b58e
    Status: Downloaded newer image for debian:jessie

(result)   > docker images
    REPOSITORY   TAG      IMAGE ID        CREATED      SIZE
    debian       jessie   f50f9524513f    5 days ago   125.1 MB
    debian       latest   f50f9524513f    5 days ago   125.1 MB
```
If you're going to run a docker image, type `docker run [image]`, but if you haven't download the image, docker will automatically pull the image from docker hub and then run it in your device.
```
(example)   > docker run nginx
```
To show all of running docker images on your machine, then type `docker ps` or if you going to show all of the docker containers whatever run or not, then type `docker ps -a`. Then if you're going to stop it then type `docker stop [NAMES]`.
```
(example)   > docker ps

or 

(example)   > docker ps -a

stop

(example)   > docker stop silly_sammet
```
To remove exceded container, you can use `docker rm [NAMES]`
```
(example)   > docker rm silly_sammet
```
To show all of list images, then use `docker images`
```
(example)   > docker images
```
To remove a docker images from your device, then you can use `docker rmi [REPOSITORY]`
```
(example)   > docker rmi nginx
```

##### **Case**
Example
```
> docker run ubuntu
> docker ps
    The container doesn't run
> docker ps -a
    The status is Exited (0)
```
Run docker image on simple web application
```
> docker run kodekloud/simple-webapp
# it will be run in foreground or attach mode, you will be attached to the console. You won't be able to do anything else on this console other than view the output until this docker container stops it, it won't response to your inputs. Press ctrl + C to stop the container. 
```
You can also run the docker container in the detacth mode and it will run the docker container in the background mode and you will be backt to your prompt immedietely, the continer will continue to run in the backend, run the docker PS command to view the running container.
```
> docker run -d kodekloud/simple-webapp
    a043d40f85......
``` 
If you would like to attach back to the running container later run the docker attach command and specify the name or ID of the docker container.
```
> docker attach a043d
```

#### **KODEKLOUD DOCKER LAB**
Go to https://kodekloud.com/p/docker-labs 
**Lab 1-3. Docker Basic Commands, Docker Run Commands, Environment Variables**
```
> docker version
> docker ps
> docker images
> docker run redis
> ctrl + C
> docker ps -a
> docker stop 63104cee8d6f
> docker rm 63104cee8d6f
> docker rmi ubuntu
> docker pull nginx:1.14-alpine
> docker run --name webapp nginx:1.14-alpine
> docker rmi mysql:latest
> docker run -p 38282:8080 kodekloud/simple-webapp:blue
> docker inspect a6144d533eb5

# Run a container named blue-app using image kodekloud/simple-webapp and set the environment variable APP_COLOR to blue. Make the application available on port 38282 on the host. The application listens on port 8080.
> docker run -p 38282:8080 --name blue-app -e APP_COLOR=blue -d kodekloud/simple-webapp
# View the application by clicking the link HOST:38282 above your terminal and ensure it has the right color
```
**Lab 4. Docker Images**
```
# Deploy a mysql database using the mysql image and name it mysql-db. Set the database password to use db_pass123.
> docker run -d -e MYSQL_ROOT_PASSWORD=db_pass123 --name mysql-db mysql

# To inspect the DockerFile that downloaded 
> vi /root/webapp-color/Dockerfile

# Build a docker image using the Dockerfile and name it webapp-color. No tag to be specified.
> docker build -t webapp-color .

# Run an instance of the image webapp-color and publish port 8080 on the container to 8282 on the host.
> docker run -p 8282:8080 webapp-color

# To pull a python docker images and run it 
> docker run python:3.6 cat /etc/*release*

# Build a new smaller docker image by modifying the same Dockerfile and name it webapp-color and tag it lite.
> docker build -t webapp-color:lite 

# Run an instance of the new image webapp-color:lite and publish port 8080 on the container to 8383 on the host.
> docker run -p 8383:8080 webapp-color:lite

```
**Lab 5. Command vs Entrypoint**
```
# Open the file /root/Dockerfile-mysql and inspect the ENTRYPOINT instruction
> vi /root/Dockerfile-mysql
# To Quit
> ctrl + C 
> :q!

# Run an instance of the ubuntu image to run the sleep 1000 command at startup and Run it in detached mode.
> docker run -d ubuntu sleep 1000
```
**Lab 6. Networking in Docker**
```
# Explore the current setup and identify the number of networks that exist on this system
> docker network ls

# Identify the network it is attached to running a container named alpine-1.
> docker inspect alpine-1

# Identify the subnet configured on bridge network
> docker network inspect bridge

# Run a container named alpine-2 using the alpine image and attach it to the none network.
> docker run --name alpine-2 --network=none alpine

# Create a new network named wp-mysql-network using the bridge driver. Allocate subnet 182.18.0.1/24. Configure Gateway 182.18.0.1
> docker network create --driver bridge --subnet 182.18.0.1/24 --gateway 182.18.0.1 wp-mysql-network

# Deploy a mysql database using the mysql:5.6 image and name it mysql-db. Attach it to the newly created network wp-mysql-network
# Set the database password to use db_pass123. The environment variable to set is MYSQL_ROOT_PASSWORD
> docker run -d -e MYSQL_ROOT_PASSWORD=db_pass123 --name mysql-db --network wp-mysql-network mysql:5.6

# Deploy a web application named webapp, using image kodekloud/simple-webapp-mysql. Expose port to 38080 on the host. The application takes an environment variable DB_Host that has the hostname of the mysql database. Make sure to attach it to the newly created network wp-mysql-network
> docker run --network=wp-mysql-network -e DB_Host=mysql-db -e DB_Password=db_pass123 -p 38080:8080 --name webapp --link mysql-db:mysql-db -d kodekloud/simple-webapp-mysql
```
**Lab 7. Storage in Docker**
```
# Run a mysql container named mysql-db using the mysql image. Set database password to db_pass123
> docker run -d --name mysql-db -e MYSQL_ROOT_PASSWORD=db_pass123 mysql

# To view the information writen in database, run the get-data.sh script available in the /root directory. 
> sh get-data.sh 

# Run a mysql container again, but this time map a volume to the container so that the data stored by the container is stored at /opt/data on the host.
# Use the same name : mysql-db and same password: db_pass123 as before. Mysql stores data at /var/lib/mysql inside the container.
> docker run -v /opt/data:/var/lib/mysql -d --name mysql-db -e MYSQL_ROOT_PASSWORD=db_pass123 mysql

# Run the get-data.sh script to ensure data is present.
> sh get-data.sh

# Disaster strikes.. again! And the database crashed again. But this time we have the data stored at /opt/data directory. Re-deploy a new mysql instance using the same options as before.
> docker run -v /opt/data:/var/lib/mysql -d --name mysql-db -e MYSQL_ROOT_PASSWORD=db_pass123 mysql

# Fetch data and make sure it is present.
> sh get-data.sh
```
**Lab 8. Docker Compose**
```
# First create a postgress database container called db, image postgres, environmental variable POSTGRES_PASSWORD=mysecretpassword
> docker run --name db -e POSTGRES_PASSWORD=mysecretpassword -d postgres

# Next let's create a simple wordpress container called wordpress, image: wordpress, link it to the container db and expose it on host port 8085
> docker run -d --name=wordpress --link db:db -p 8085:80 wordpress
```
####**Docker Run**
If you use `docker run redis`, then you will run redis with the latest version of redis. But, if you going to run the redis with different version, then you specify:
```
> docker run redis:4.0
```
**RUN - Standard Input**
If you have a file with input statetement and run it manually using terminal, then you will get:
```
~/prompt-application$./app.sh
Welcome! Please enter your name: Mumshad

Hello and Welcome Mumshad!
```
But, if you try to run it using docker. Then you will unable to give the input statement:
```
> docker run kodekloud/simple-prompt-docker

Hello and Welcome !
```
Docker container, doen't listen to it's standard input, eventhough you attach your console, they unable to read any input from you, they doesn't have a terminal to read in what's input from. It runs in a non interactive mode. If you want to add inputs, you must map the standard input in your host to the docker container using the following command
```
> docker run -i kodekloud/simple-prompt-docker
Mumshad

Hello and Welcome Mumshad!
```
But, it still can't print the text command, so you can add `-it`
```
> docker run -it kodekloud/simple-prompt-docker
Welcome! Please enter your name: Mumshad

Hello and Welcome Mumshad!
``` 
**RUN - Port Mapping**
if you run containerize webapp
```
> docker run kodekloud/webapp
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
But you don't know where is the IP address
```
If your IP: 192.168.1.5
Webapp Container IP in your local: 192.168.1.5:80
Webapp Container IP from Docker host: 172.17.0.2:5000
```
Then you can run the webapp as many as possible using port mapping
```
> docker run -p 80:5000 kodekloud/simple-webapp
> docker run -p 8000:5000 kodekloud/simple-webapp
> docker run -p 8001:5000 kodekloud/simple-webapp
> docker run -p 3306:3306 kodekloud/simple-webapp
> docker run -p 8306:3306 kodekloud/simple-webapp
```
**RUN - Volume Mapping**
When you run MySQL in docker container, then the data will be stored in docker container library
```
> docker run mysql
~/var/lib/mysql
```
If you stop and delete the container, it will make your data blown away.
```
> docker stop mysql
> docker rm mysql
```
To mitigate that, you can move the data from the container to the outside of the container
```
> docker run -v /opt/datadir:/var/lib/mysql mysql
(stored) ~/opt/datadir
```
**Inspect Container**
```
> docker inspect blissfull_hopper
```
**Container Logs**
```
> docker logs blissful_hopper
```
### **DOCKER ENVIRONMENT VARIABLES**
For example you have a simple web application name `app.py`, and it display the webpage with `red` background color. And if you decide to change the color in the future, you have to change the application code. The best practice to move such information out of the application code and into say environment variable called:
```
app.py

(before) color = 'red'
(after)  color = os.environ.get('APP_COLOR')

> export APP_COLOR = blue; python app.py
```
it will packed in docker image and run it using following command
```
> docker run simple-webapp-color

# If you pass the environment variable before you can do
> docker run -e APP_COLOR=blue simple-webapp-color

# You can run the webapp each time
> docker run -e APP_COLOR=red simple-webapp-color
> docker run -e APP_COLOR=green simple-webapp-color
> docker run -e APP_COLOR=pink simple-webapp-color
```
**Inspect Environment Variable**
```
> docker inspect blissful_hopper
# you can find the "Env" : ["APP_COLOR=blue",...] 
```
### **DOCKER IMAGES**
You need to create your own docker images because it will help you to shipping and deployment.
If you don't create docker images and do it manually, then you need to:
1. OS - Ubuntu
2. Update apt repo
3. Install dependencies using apt
4. Install Python dependencies using pip
5. Copy source code to /opt folder
6. Run the web server using `flask` command

### **6. Create a Docker Image**
If youw want to run the following step in docker, then you need to:
1. create dockerfile
```
FROM Ubuntu

RUN apt-get update
RUN apt-get install python

RUN pip install flask
RUN pip install flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
``` 
then you can build you docker image using docker command and specify the docker file as input as well as the tag name for the image
```
> docker build Dockerfile -t mmumshad/my-custom-app
```
this will create an image locally on your system, to make it available on the public docker hub registry, run the docker push command and specify the imange name
```
> docker push mmumshad/my-custom-app
```
**Dockerfile** : is a text file written in a specific format that docker can understand it's in an instruction and arguments format. For example in this docker file, the `UPPER CASE` command is the `INSTRUCTION`, and the `LOWER CASE` command is the `ARGUMENT`. For example:
```
# Start from a base OS or another image
FROM Ubuntu

# Install all dependencies
RUN apt-get update
RUN apt-get install python

RUN pip install flask
RUN pip install flask-mysql

# Copy source code
COPY . /opt/source-code

# Specify Entrypoint
ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```
**Layered Architecture**
```
# Layer 1. Base Ubuntu Layer
FROM Ubuntu

# Layer 2. Changes in apt packages
RUN apt-get update && apt-get -y install python

# Layer 3. Changes in pip packages 
RUN pip install flask flask-mysql

# Layer 4. Source code
COPY . /opt/source-code

# Layer 5. Update Entrypoint with "flask" command
ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```
You can see the docker history to see the image size for each layer
```
> docker history mmumshad/simple-webapp
```
If you run the docker build command you will see the steps involved and the result of each task, all the layer built are cast so the layered architecture helps you restart docker built from that particular step in case it fails or if you were to add new steps in build process you wouldn't start all over again. 

### **DOCKER CMD vs ENTRYPOINT**
When you run docker images, it will run the image and exit immedietely. 
```
> docker run ubuntu
> docker ps
> docker ps -a
```
Unlike virtual machine, containers are not meant to host an operating system. Containers are meant to run a specific task or process such as application, database, or aplication. The container will exist as long as the container is a live, if the web service inside the container is dot or crashes, the container exit. 

If we run the ubuntu container earlier, docker will create a container from the ubuntu image and launch the bash program, by default docker does not attach a terminal to container when it is run and so the bash program doesn't find the terminal and so it exits.

```
> docker run ubuntu [COMMAND]
> docker run ubuntu sleep 5
```
If you want make it a permanent
```
FROM Ubuntu

CMD sleep 5
CMD ['sleep','5']
```
then I want to build my new image using docker build command and name it as ubuntu sleeper
```
> docker build -t ubuntu sleeper .
> docker run ubuntu-sleeper
```
it will sleep 5 seconds and the exit. You can also make it into
```
FROM Ubuntu

CMD sleep 5

> docker run ubuntu-sleeper sleep 10

FROM Ubuntu

ENTRYPOINT ["sleep"]

> docker run ubuntu-sleeper 10
sleep 10

# if you run 
> docker run ubuntu-sleeper
(ERROR)

FROM Ubuntu

ENTRYPOINT['sleep']

CMD['5']

> docker run --entrypoint sleep2.0 ubuntu-sleeper 10
sleep2.0 10
```
### **DOCKER NETWORKING**
### **7. Networks in Docker**
**Default Network**
```
(Bridge) > docker run ubuntu
(none)   > docker run ubuntu --network=none
(host)   > docker run ubuntu --network=host
```
**User-defined Network**
```
> docker network create \
    --driver bridge \
    --subnet 182.18.0.0/16
    custom-isolated-network
```
to see all of docker network
```
> docker network ls
```
**Inspect Network**
```
> docker inspect blissful_hopper
"bridge":{
    "Gateway": "172.17.0.1",
    "IPAddress": "172.17.0.6"
    "MacAddress": "02:42:ac:11:00:06",
}
```
**Embedded DNS**
container can reach each other using their names for example in this case I have a `webserver` and `MySQL database` container running on the same node
```
-------------     -----------------
|    WEB    |     |     MySQL     |
| Container |     |   Container   |
-------------     -----------------
      |172.17.0.2         |172.17.0.3
      |                   |
      |------ Docker -----|

> mysql.connect(172.17.0.3)
> mysql.connect(mysql)
```
The name of the container docker has a built-in DNS server that helps the containers to resolve each other using the container name. Built in `DNS Server` always runs at address `127.0.0.11`. Docker create name space for each container it then uses virtual Ethernet pairs to connect containers together.

### **DOCKER STORAGE**
Docker file system:
```
~/var/lib/docker
    - aufs
    - containers
    - image
    - volumes
```
Docker layered architecture, let's quickly recap something we learned when docker builds images it builds these in a layered architecture. Each line of instruction
```
# Layer 1. Base Ubuntu Layer
FROM Ubuntu

# Layer 2. Changes in apt packages
RUN apt-get update && apt-get -y install python

# Layer 3. Changes in pip packages 
RUN pip install flask flask-mysql

# Layer 4. Source code
COPY . /opt/source-code

# Layer 5. Update Entrypoint with "flask" command
ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
``` 
```
> docker build Dockerfile -t mmumshad/my-custom-app
```
consider the second application
```
# Layer 1. Base Ubuntu Layer
FROM Ubuntu

# Layer 2. Changes in apt packages
RUN apt-get update && apt-get -y install python

# Layer 3. Changes in pip packages 
RUN pip install flask flask-mysql

# Layer 4. Source code
COPY app2.py /opt/source-code

# Layer 5. Update Entrypoint with "flask" command
ENTRYPOINT FLASK_APP=/opt/source-code/app2.py flask run
```
```
> docker build Dockerfile2 -t mmumshad/my-custom-app-2
```
it only change the last 2 layer (4 & 5), and build it faster and immedietely and save disk space
**Layered Architecture**
Image Layers (Read Only)
```
# Layer 1. Base Ubuntu Layer
# Layer 2. Changes in apt packages
# Layer 3. Changes in pip packages 
# Layer 4. Source code
# Layer 5. Update Entrypoint with "flask" command
```
```
> docker run mmumshad/my-custom-app
```
Container Layer (Read Write)
```
# Layer 6. Container Layer
```
**Copy-on-write**
Image Layer (Read Only)
```
app.py
```
Container Layer
```
app.py (copied version)
temp.txt
```
the image will be same all the time until you rebuild the image using docker build command.
**volume**
```
> docker volume create data_volume
~/var/lib/data_volume

> docker run -v data_volume:/var/lib/nysql mysql
```
it will store all of mysql database data into data_volume, and when the container layer destroyed, the data will still there
### **DOCKER COMPOSE**
### **8. Docker Compose**
### **9. Docker Concepts in Depth**
### **10. Docker for Windows/Mac**
### **11. Docker Swarm**
### **12. Docker Kubernetes**
### **13. Conclusion**

https://www.youtube.com/watch?v=3c-iBn73dDE
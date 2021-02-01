# **2 Hours NGINX Crash Course**

Course Link : [2 Hours NGINX Crash Course + Bonus Content (Audio Fixed)](https://www.youtube.com/watch?v=hcw-NjOh8r0)

### **Agenda**
- What is NGINX?
- Current & Desired Architecture
- Layer 4 and Layer 7 Proxying in NGINX
- Example: 
    - NGINX as a Web Server, Layer 7 and Layer 4 Proxy
    - Enable HTTPS, TLS 1.3 & HTTP/2 on NGINX
- Summary

### **What is NGINX?**
- Web Server
    - Server Web Content
- Proxy 
    - Load Balancing
    - Backend Routing
    - Caching

### **Current Architecture & Database**
```
Customer --> Get /employees --> Server <-> db:5432
```
This server to busy and you need to move to other ports

And in here you need NGINX, so you have server and you have NGINX in the surface to manage all of port balancing 
```
Customer --> GET /employees --> NGINX (HTTPS:443, h/2) --> Server (ports) <-> db:5432
Customer <-- JSON {} <-- NGINX (HTTPS:443, h/2) <-- Server (ports) <-> db:5432
```

NGINX will connect you from frontend to backend (database)

### **Layer 4 and Layer 7 proxying in NGINX**
- NGINX can operate in layer 7 (http) or layer 4 (tcp)
- Using *stream* context it becomes layer 4 proxy
- Using *http* context it becomes layer 7 proxy
In NGINX, You can act like layer 4 and layer 7 proxy

### **Example**
- Install NGINX (Mac) 
- NGINX as a Web Server
- NGINX as a Layer 7 Proxy
    - Proxy to 4 Backend NodeJS services (docker)
    - split load to multiple backend (app1/app2)
    - Block certain requests (/admin)
- NGINX as a layer 4 Proxy
- Enable HTTPS on NGINX (lets encrypt)
- Enable TLS 1.3 on NGINX 
- Enable HTTP/2 on NGINX

### **Install NGINX (Mac)**
```
$ brew install nginx
nginx will load all files in /usr/local/etc/nginx/servers/.

# Delete file and create new from scratch
$ cd /user/local/etc/nginx
$ ls
$ vim nginx.conf
$ rm nginx.conf
$ vim nginx.conf
```
Will open new command line (files) and create new server configuration
```
http {

    server {
        listen 8080;
    }
}

events { }
```
and save it, by quit `:qa`. And how to start running the NGINX? back to the command line and type `nginx`
```
$ nginx
```

And go to localhost:8080, you can see that a static files. It will show a static files and it will give a default stuff. and let's change that it. Let's create a folder inside the nginx folder location.
```
$ ls
$ cd /Users/HusseinNasser/ (outside NGINX folder)
$ mkdir nginxcourse
$ ls
$ vim index.html
```
Create a html file
```html
<html>
<body>
hello its nginx but it's my own context
</body>
</html>
```

### **Static Context Location Root**
Back again into shell
```
$ cd /user/local/etc/nginx
$ ls
$ vim nginx.conf
```
and change some configuration
```
http {

    server {
        listen 8080;
        root /Users/HusseinNasser/nginxcourse/
    }
}

events { }
```
You need to stop the first running nginx and start it again
```
$ nginx -s stop
$ nginx
```
Now, back to the `localhost:8080`, you can see the html file running in the local host

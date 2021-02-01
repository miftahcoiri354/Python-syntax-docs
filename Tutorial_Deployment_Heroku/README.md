# **Deployment Heroku**

1. Download & Install Heroku CLI
2. Create Account & Login into Heroku CLI
3. Open CLI :

Then Follow this Instructions:
```
> heroku
> heroku login

# To push our images to docker registry you must to login in heroku container registry 
> heroku container:login

# make sure you run it in app directory with docker image  
> heroku create
Creating app... done, (stormy-headland-40304)
https://stormy-headland-40304.herokuapp.com/ | https://.heroku.com/stormy-headland-40304.git

# Build and push the images into Heroku registry
> heroku container:push web --app stormy-headland-40304
It will build the image

# Now open the heroku app and visit the browser
> heroku open --app stormy-headland-40304
```

Then go to web browser and copy the url
```
https://stormy-headland-40304.herokuapp.com/
```
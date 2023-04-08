sudo apt-get upgrade -y
sudo apt-get update
sudo apt install nginx -y

nano firewall.sh

#!/bin/bash
sudo ufw allow ssh
sudo ufw allow 22
sudo ufw allow 443
sudo ufw allow 8080
sudo ufw allow 80
sudo ufw status
sudo ufw enable

bash firewall.sh

sudo mkdir /var/www/html/ztechonoid.com
sudo mkdir /var/www/html/api.ztechonoid.com
sudo mkdir /var/www/html/jenkins.ztechonoid.com

sudo chown -R www-data:www-data /var/www/html/ztechonoid.com
sudo chown -R www-data:www-data /var/www/html/api.ztechonoid.com
sudo chown -R www-data:www-data /var/www/html/jenkins.ztechonoid.com

sudo nano /var/www/html/ztechonoid.com

```
<html>
	<head>
	  <title>Welcome to ztechonoid.com!</title>
  </head>
	  <body>
	    <h1>Congratulations! The ztechonoid.com website is working!</h1>
    </body>
</html>
```

sudo nano /etc/nginx/sites-available/ztechonoid.com

```
server {
        listen 80;
        root /var/www/html/ztechonoid.com;
        index index.html index.htm;
        server_name ztechonoid.com;
        location / {
            try_files $uri $uri/ =404;
        }
    }
```

sudo nano /etc/nginx/sites-available/jenkins.ztechonoid.com

```
server {
        listen 80;
        root /var/www/html/jenkins.ztechonoid.com;
        index index.html index.htm;
        server_name jenkins.ztechonoid.com;
        location / {
            proxy_pass http://127.0.0.1:8080;
            include proxy_params;
            try_files $uri $uri/ =404;
        }
    }
```

sudo nano /etc/nginx/sites-available/api.ztechonoid.com

```
server {
        listen 80;
        root /var/www/html/api.ztechonoid.com;
        index index.html index.htm;
        server_name api.ztechonoid.com;
        location / {
            proxy_pass http://127.0.0.1:3000;
            include proxy_params;
            try_files $uri $uri/ =404;
        }
    }
```

sudo nginx -t

sudo ln -s /etc/nginx/sites-available/ztechonoid.com /etc/nginx/sites-enabled/

sudo ln -s /etc/nginx/sites-available/jenkins.ztechonoid.com /etc/nginx/sites-enabled/

sudo ln -s /etc/nginx/sites-available/api.ztechonoid.com /etc/nginx/sites-enabled/

sudo systemctl restart nginx

##

sudo apt-get install certbot python3-certbot-nginx -y

sudo certbot certonly --agree-tos --email myemail@email.com -d awstutorial.net

### Install Docker

https://docs.docker.com/engine/install/ubuntu/
sudo apt install docker-compose -y

sudo docker network create jenkins

nano Dockerfile

```
FROM jenkins/jenkins:2.387.2
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
```

docker build -t myjenkins-blueocean:2.387.2-1 .

```
docker run --name jenkins-blueocean --restart=on-failure --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.387.2-1
```

sudo docker container exec -it jenkins-blueocean bash

cat /var/jenkins_home/secrets/initialAdminPassword

copy and paste in http://localhost:8080/

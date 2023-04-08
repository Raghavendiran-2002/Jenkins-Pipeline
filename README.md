# Jenkins-Pipeline

## Install Dependency

```
sudo apt-get upgrade -y
sudo apt-get update
sudo apt install nginx -y
sudo apt-get install certbot python3-certbot-nginx -y
```

## Enable Firewall

nano firewall.sh

```
#!/bin/bash
sudo ufw allow ssh
sudo ufw allow 22
sudo ufw allow 443
sudo ufw allow 8080
sudo ufw allow 80
sudo ufw status
sudo ufw enable
```

bash firewall.sh

## Configure Nginx Server

```
sudo mkdir /var/www/html/ztechonoid.com
sudo mkdir /var/www/html/api.ztechonoid.com
sudo mkdir /var/www/html/jenkins.ztechonoid.com
```

```
sudo chown -R www-data:www-data /var/www/html/ztechonoid.com
sudo chown -R www-data:www-data /var/www/html/api.ztechonoid.com
sudo chown -R www-data:www-data /var/www/html/jenkins.ztechonoid.com
```

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

###### DNS Record

```
Hostname = "" ; Type : A ; TTL : 1 hr ; Data/IP : <IP-ADDRESS>
Hostname = "jenkins" ; Type : A ; TTL : 1 hr ; Data/IP : <IP-ADDRESS>
Hostname = "api" ; Type : A ; TTL : 1 hr ; Data/IP : <IP-ADDRESS>
```

sudo nginx -t

sudo ln -s /etc/nginx/sites-available/ztechonoid.com /etc/nginx/sites-enabled/

sudo ln -s /etc/nginx/sites-available/jenkins.ztechonoid.com /etc/nginx/sites-enabled/

sudo ln -s /etc/nginx/sites-available/api.ztechonoid.com /etc/nginx/sites-enabled/

sudo systemctl restart nginx

#### SSL

sudo certbot certonly --agree-tos --email myemail@email.com -d awstutorial.net
https://adamtheautomator.com/nginx-subdomain/

## Install Docker

https://docs.docker.com/engine/install/ubuntu/

sudo apt install docker-compose -y

## Install Jenkins

create Docker Network for Jenkins

```
sudo docker network create jenkins
```

create a Dockerfile

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

Build Docker image

```
docker build -t myjenkins-blueocean:2.387.2-1 .
```

Run Docker image

```
docker run --name jenkins-blueocean --restart=on-failure --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.387.2-1
```

## Configure Jenkins

Docker(jenkins-blueocean) Termial

```
sudo docker container exec -it jenkins-blueocean bash
```

To copy the Admin Key

```
cat /var/jenkins_home/secrets/initialAdminPassword
```

copy and paste in http://localhost:8080/

## create Pipeline

- create New Project
- choose "Pipeline" && enter project name
- under "Build Triggers" select "Github hook trigger for GITScm polling"
- under "Pipeline" choose "Pipeline script from SCM"
- under "SCM" choose "git"
- under "Repository URL" enter Github URL
- under "Credentials" click "Add" choose "Jenkins"
- "Jenkins Credentials Provider" pops-up
- under "Username" enter github username
- under "Password" enter github personal token
- under "Description" enter the description
- once the "Credentials Provider" closes
- choose "Credentails" which you have created above
- under "Branches to build" specify the branch name
- click "Apply and Save"

##### Webhooks setup

- choose "user" on right-top near logout
- choose "configure"
- under "API Token" > add new token > copy the token
- Add the token on to github > under repo "settings" > under "code and automations" > select "Webhooks"
- click "Add Webhooks"
- under "Payload URL" > IP-ADDRESS-SERVER/github-webhook/
- under "content type" > "application/json"
- paste the above token under "Secret"
- click "create webhook"

https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Jenkins-GitHub-Webhook-example-no-403-crumb-error

## Jenkins

https://www.youtube.com/watch?v=HSA_mZoADSw

Port Forward : https://medium.com/automationmaster/how-to-use-ngrok-to-forward-my-local-port-to-public-5e9b148ff31c

```
ngrok http 8080
```

https://www.cloudbees.com/blog/jenkins-tutorial-configure-scm-github-triggers-and-git-polling-using-ngrok

https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Jenkins-GitHub-Webhook-example-no-403-crumb-error

Alternative for Ngrok
http://serveo.net/

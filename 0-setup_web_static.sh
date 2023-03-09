#!/usr/bin/env bash
# This script sets up nginx web server for deployment of web_static

# Install Nginx if it not already installed
sudo apt install nginx -y

# Create folder /data/web_static/shared if it doesn't exist
sudo mkdir -p /data/web_static/shared/
# Create folder /data/web_static/releases/test if it doesn't exist
sudo mkdir -p /data/web_static/releases/test/
# Create fake HTML file /data/web_static/releases/test/index.html
sudo touch /data/web_static/releases/test/index.html
# Write simple HTML code to fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body> " > /data/web_static/releases/test/index.html

# Create symbolic link /data/web_static/current linked to /data/web_static/releases/test

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
sudo useradd -m ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
# (ex: https://mydomainname.tech/hbnb_static)
# Create a Nginx configuration file
sudo touch /etc/nginx/sites-available/default
# Write Nginx configuration to file
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
    location / {
        try_files $uri $uri/ =404;
    }
}" > /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart


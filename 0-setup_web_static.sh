#!/usr/bin/env bash
# This script sets up nginx web server for deployment of web_static

# Install Nginx if it not already installed
sudo apt-get --fix-missing update 
sudo apt install nginx -y

# Create folder /data/web_static/shared if it doesn't exist
sudo mkdir -p /data/web_static/shared/
# Create folder /data/web_static/releases/test if it doesn't exist
sudo mkdir -p /data/web_static/releases/test/
# Create fake HTML file /data/web_static/releases/test/index.html
sudo touch /data/web_static/releases/test/index.html
# Write simple HTML code to fake HTML file
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body> " > /data/web_static/releases/test/index.html

# Create symbolic link /data/web_static/current linked to /data/web_static/releases/test

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group

# Create a Nginx configuration file
# sudo touch /etc/nginx/sites-available/default
# change the owner of default file to ubuntu
sudo chown -R ubuntu:ubuntu /etc/nginx/sites-available/default
sudo chown -R ubuntu:ubuntu /data
# Write Nginx configuration to file
sudo sed -i '/listen 80 default_server;/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
# Restart Nginx
sudo service nginx restart


#!/usr/bin/env bash

# Update package lists and install Nginx if it's not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create the necessary directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file in index.html
echo "<html>
  <head>
  </head>
  <body>
    Konyhea
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, if it already exists, it will be recreated
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of /data/ to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

#!/usr/bin/env bash
# install and configure nginx
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y
sudo service nginx start
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton school\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R "$USER":"$USER" /data/
loc="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html index.htm;\n\t}"
sed -i "62i $loc" /etc/nginx/sites-available/default
sudo service nginx restart

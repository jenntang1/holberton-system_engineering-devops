# This manifest installs Ngnix.
exec { 'ngnix':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx && sudo echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html && var="rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" && sudo sed -i "35i$var" /etc/nginx/sites-available/default && sudo service nginx start',
  provider => shell
}

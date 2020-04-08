# This manifest adds a custom HTTP header.
exec { 'http':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx && sudo echo "Holberton School for the win!" | sudo tee /var/www/html/index.nginx-debian.html && var="rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" && sudo sed -i "35i$var" /etc/nginx/sites-available/default && sudo echo "Ceci n\'est pas une page" | sudo tee /var/www/html/custom_404.html && var2="error_page 404 /custom_404.html;\nlocation /custom_404.html {\nroot /var/www/html;\ninternal;\n}" && sudo sed -i "36i$var2" /etc/nginx/sites-available/default && var4="add_header X-Served-By $HOSTNAME;" && sudo sed -i "41i$var4" /etc/nginx/sites-available/default && sudo service nginx start',
  provider => shell
}

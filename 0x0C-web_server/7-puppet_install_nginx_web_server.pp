# This manifest installs Ngnix.
exec { 'ngnix':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx && echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html && sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default-backup && var="\tserver_name jenntang1.tech;\n\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" && sudo sed -i "35i\ $var" /etc/nginx/sites-available/default && sudo service nginx start',
  provider => shell
}

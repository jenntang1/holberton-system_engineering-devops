# This manifest resolves heavy HTTP requests.  

exec { 'fix--for-nginx':
  command  => 'sudo echo "nginx\t soft\t nofile\t 30000\nnginx\t hard\t nofile\t 50000\n"'\
              ' | sudo tee -a /etc/security/limits.conf && sudo service nginx restart',
  provider => shell
}

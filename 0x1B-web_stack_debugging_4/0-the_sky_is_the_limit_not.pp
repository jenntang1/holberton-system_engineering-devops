# This manifest resolves heavy HTTP requests.

exec { 'fix--for-nginx':
  command  => 'sudo sed -i "4iworker_rlimit_nofile 500000\n" /etc/nginx/nginx.conf && '\
              'sudo echo "nginx\tsoft\tnofile\t500000\nnginx\thard\tnofile\t500000\n"'\
              ' | sudo tee -a /etc/security/limits.conf && sudo service nginx restart',
  provider => shell
}

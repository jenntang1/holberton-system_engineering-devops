# This manifest resolves heavy HTTP requests.

exec { 'fix--for-nginx':
  command  => 'sudo sed -i "12iLimitNOFILE" /lib/systemd/system/nginx.service '\
              '&& sudo service nginx restart',
  provider => shell
}

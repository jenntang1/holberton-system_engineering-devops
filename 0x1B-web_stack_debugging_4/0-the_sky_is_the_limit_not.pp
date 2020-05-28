# This manifest resolves heavy HTTP requests.

exec { 'fix--for-nginx':
  command  => 'sudo sed -i "s/15/5000/g" /etc/default/nginx',
  provider => shell
}

# This manifest resolves heavy HTTP requests.

exec { 'fix--for-nginx':
  command  => 'sudo sed -i "s/-n */-n 5000000/g" /etc/default/nginx',
  provider => shell
}

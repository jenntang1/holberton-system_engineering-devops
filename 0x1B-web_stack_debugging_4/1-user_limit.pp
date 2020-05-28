# This manifest resolves heavy HTTP requests.

exec { 'change-os-configuration-for-holberton-user':
  command  => 'sudo sed -i "s/nofile */nofile 50000/g" /etc/security/limits.conf',
  provider => 'shell'
}

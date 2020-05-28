# This manifest resolves heavy HTTP requests.  

exec { 'change-os-configuration-for-holberton-user':
  command  => 'sudo sed -i "s/holberton hard nofile 5/holberton hard nofile 50000/g" /etc/security/limits.conf'\
              ' && sudo sed -i "s/holberton soft nofile 4/holberton soft nofile 50000/g" /etc/security/limits.conf'\
              ' && sudo service nginx restart',
  provider => shell
}

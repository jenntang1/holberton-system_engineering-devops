# This manifest sets up a SSH config file.
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/holberton',
  match => 'IdentityFile *'
}
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => 'PasswordAuthentication yes'
}

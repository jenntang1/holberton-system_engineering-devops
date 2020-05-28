# This manifest resolves heavy HTTP requests.

include limits
limits::limit { 'user limit':
  domain => 'holberton',
  item   => 'nofile',
  value  => '50000'
}

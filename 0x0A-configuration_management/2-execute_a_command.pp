# This manifest creates a manifest that kills a process.
exec { 'killmenow':
  command  => 'pkill killmenow',
  path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
  provider => 'shell'
}

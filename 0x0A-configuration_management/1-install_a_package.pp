# This manifest installs puppet-lint 2.1.1.
package { 'puppet-lint':
  ensure   => ['created', '2.1.1'],
  provider => 'gem'
}

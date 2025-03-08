# Puppet script to fix 'Too many open files' error for the holberton user
# This script increases file descriptor limits and ensures proper session settings.

file { '/etc/security/limits.conf':
  ensure  => present,
  content => "* hard nofile 65535\n* soft nofile 65535\n",
}

file { '/etc/pam.d/common-session':
  ensure  => present,
  content => "session required pam_limits.so\n",
  append  => true,
}

exec { 'reload-limits':
  command     => '/sbin/sysctl -p',
  refreshonly => true,
}

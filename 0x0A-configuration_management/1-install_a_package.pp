# Installs flask from pip3

exec { 'add-python3.8-ppa':
  command => '/usr/bin/add-apt-repository -y ppa:deadsnakes/ppa && /usr/bin/apt-get update',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  unless  => 'test -f /etc/apt/sources.list.d/deadsnakes-ubuntu-ppa-focal.list',
}

package { 'python3.8':
  ensure   => '3.8.10',
  provider => 'apt',
  require  => Exec['add-python3.8-ppa'],
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['Flask'],
}

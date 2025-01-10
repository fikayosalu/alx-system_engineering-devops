# Create a file 'school' with contents 'I love Puppets' in /tmp

file { 'school file':
  ensure  => 'present',
  path    => '/tmp/school',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0774',
  content => 'I love Puppet'
}

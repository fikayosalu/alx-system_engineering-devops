# Create a file 'school' with contents 'I love Puppets' in /tmp

file { '/tmp/school':
  owner   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}

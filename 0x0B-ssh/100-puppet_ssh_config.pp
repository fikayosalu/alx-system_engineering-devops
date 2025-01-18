# Make changes to client SSH configuration file
file_line{ 'no password':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no'
}

file_line{ 'private key path':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school'
}

# Make changes to client SSH configuration file
file_line{ 'no password':
  path  => '~/.ssh/config',
  line  => 'PasswordAuthentication no'
}

file_line{ 'private key path':
  path  => '~/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school'
}

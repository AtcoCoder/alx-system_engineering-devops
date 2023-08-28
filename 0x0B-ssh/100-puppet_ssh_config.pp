# Make changes to our ssh configuration file

file_line { 'Append a line':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
}

file_line { 'Append a line':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '    IndentityFile ~/.ssh/school',
}

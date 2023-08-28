# Make changes to our ssh configuration file
include stdlib

file { 'Check file',
  ensure  => 'file',
  path    => '~/etc/ssh/ssh_config',
  replace => true,
}->
file_line { 'Append a line':
  path    => '~/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
}->
file_line { 'Append a line':
  path    => '~/etc/ssh/ssh_config',
  line    => '    IndentityFile ~/.ssh/school',
  replace => true,
}

# Make changes to our ssh configuration file
include stdlib

file { 'Check file',
  ensure  => 'file',
  path    => '~/etc/ssh/sshd_config',
  replace => true,
}->
file_line { 'Append a line':
  path    => '~/etc/ssh/sshd_config',
  line    => '\tPasswordAuthentication no',
}->
file_line { 'Append a line':
  path    => '~/etc/ssh/sshd_config',
  line    => '\tIndentityFile ~/.ssh/school',
  replace => true,
}

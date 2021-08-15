$mytext = "Host 34.75.72.161
     PasswordAuthentication no
     IdentityFile ~/.ssh/holberton"

file {'~/.ssh/.config':
  ensure  => file,
  path    => '~/.ssh/.config',
  content => $mytext,
}

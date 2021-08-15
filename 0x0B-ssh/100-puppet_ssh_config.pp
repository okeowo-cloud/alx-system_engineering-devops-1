define accounts_global::account () {

  account { $name:
    ensure => present,
  }
$mytext = "Host 34.75.72.161
     PasswordAuthentication no
     IdentityFile ~/.ssh/holberton"

file { "/home/${name}/.ssh/config" :
  ensure  => file,
  path    => '/home/${name}/.ssh/config',
  content => $mytext,
}

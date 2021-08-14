# use 'exec' and 'pkill'

exec { 'killmenow':
  command => '/usr/bin/pkill -f /killmenow',
}

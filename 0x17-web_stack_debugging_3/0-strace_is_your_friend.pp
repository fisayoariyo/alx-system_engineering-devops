# fixes a bug in wp-setings.php
# by replacing mistyped word in /var/www/html/wp-settings.php
#
exec { 'fix the php extension issue':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/',
}

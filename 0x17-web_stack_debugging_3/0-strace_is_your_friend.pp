# This manifest resolves a Wordpress 500 error.

exec { 'fix-wordpress':
	command  => 'sudo sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php && sudo service apache2 restart',
	provider => shell
}

# Install and configure nginx on my server

# Run update
exec { 'run update':
  command  => 'apt-get -y update',
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => 'shell',
}

# Ensure that nginx is instelled.
package { 'nginx':
  ensure          => 'installed',
  provider        => 'apt',
  install_options => ['-y'],
}


# the landing page
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

# the 404 page
file { '/var/www/html/404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page",
}

$server_configuration = "server {
	listen 80;
	listen [::]:80;
	server_name _;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	error_page 404 /404.html;

	location /404.html {
		internal;
	}

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	location / {
		try_files \$uri \$uri/ =404;
	}
}"

# Configure the server
file { '/etc/nginx/sites-available/default':
  content => $server_configuration,
}

# Restart the server
exec { 'server_restart':
  command  => 'service nginx restart',
  provider => 'shell',
}

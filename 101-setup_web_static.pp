# Update package lists and install Nginx if it's not already installed
package { 'nginx':
  ensure => installed,
  require => Exec['apt_update'],
}

exec { 'apt_update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
}

# Create the necessary directories if they don't already exist
file { '/data':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
  require => File['/data'],
}

file { '/data/web_static/releases':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
  require => File['/data/web_static'],
}

file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
  require => File['/data/web_static/releases'],
}

file { '/data/web_static/shared':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
  require => File['/data/web_static'],
}

# Create a fake HTML file in index.html
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
  <head>
  </head>
  <body>
    Konyhea
  </body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  require => File['/data/web_static/releases/test'],
}

# Create a symbolic link, if it already exists, it will be recreated
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => File['/data/web_static/releases/test'],
}

# Update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

# Nginx configuration template
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}
",
}
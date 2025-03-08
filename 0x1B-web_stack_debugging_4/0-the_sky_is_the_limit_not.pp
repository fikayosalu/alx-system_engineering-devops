# This Puppet script optimizes Nginx for handling high traffic by increasing worker limits, buffers, and timeouts.

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Modify Nginx configuration to optimize performance
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

# Define the optimized Nginx config template
file { '/etc/nginx/nginx.conf':
  ensure  => present,
  content => epp("
worker_processes auto;

events {
    worker_connections 1024;
    multi_accept on;
}

http {
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;

        location / {
            root /var/www/html;
            index index.html;
        }

        # Increase buffer sizes to prevent request failures
        client_body_buffer_size 128k;
        client_max_body_size 10m;
        large_client_header_buffers 4 32k;

        # Increase timeouts
        proxy_connect_timeout 75s;
        proxy_send_timeout 75s;
        proxy_read_timeout 75s;
        send_timeout 75s;
    }
}
  "),
  notify  => Service['nginx'],
}

# Restart Nginx to apply changes
exec { 'fix--for-nginx':
  command => 'systemctl restart nginx',
  path    => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
  require => File['/etc/nginx/nginx.conf'],
}


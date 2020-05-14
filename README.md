# nginx-proxy-test

The base configuration for reverse proxy (both localhost without HTTPS and public domain name with HTTPS)
The REST API server is implemented by Flask

When you access to http(s)://<address>/, it will show "this is index.html"
When you access to http(s)://<address/api/v1/test/, it will show "Flask OK"

# How to use

- For localhost without HTTPS

docker-compose -f docker-compose-simple.yml up --build -d

- For public domains with HTTPS

1. Replace "www.example.com" and "blog.example.com" with your domains.

  Ex.)
  find . -type f -print0|xargs -0 sed  -i -e "s/example.com/your.domain/g"

2. docker-compose up --build -d
This will automatically create the certification of Let's Encrypt

You need the public domains which can be resolve by DNS

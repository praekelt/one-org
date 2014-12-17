#!/bin/bash

service nginx stop

function syncdb() {
    service=$1
    cd /var/praekelt/$service/
    ./bin/$service syncdb --noinput
    ./bin/$service migrate
    ./bin/$service load_photosizes
    ./bin/$service loaddata ./org/fixtures/sites.json 
    cd -
}

function collectstatic() {
    service=$1
    cd /var/praekelt/$service/
    rm -rf static
    ./bin/$service collectstatic --noinput
    cd -
}

echo "org-live-admin-site:" > /var/praekelt/postinstall.log
syncdb org-live-admin-site >> /var/praekelt/postinstall.log 2>&1

for site in org-live-admin-site org-live-basic-site; do
    echo "$site:" >> /var/praekelt/postinstall.log
    collectstatic $site >> /var/praekelt/postinstall.log 2>&1
done

chown -R www-data:ubuntu /var/praekelt/*

supervisorctl update
supervisorctl restart org:*
service nginx start

#!/bin/bash

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
    cd /var/praekelt/$service/
    rm -rf static
    ./bin/$1 collectstatic --noinput
    cd -
}

echo "org-qa-common-site:" > /var/praekelt/postinstall.log
syncdb org-qa-common-site >> /var/praekelt/postinstall.log 2>&1

for site in org-qa-admin-site org-qa-basic-site; do
    echo "$site:" >> /var/praekelt/postinstall.log
    syncdb $site >> /var/praekelt/postinstall.log 2>&1
    collectstatic $site >> /var/praekelt/postinstall.log 2>&1
done


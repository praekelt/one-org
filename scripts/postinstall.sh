manage="${VENV}/bin/python ${INSTALLDIR}/${REPO}/manage.py"

if [ ! -f ${INSTALLDIR}/one-org-installed ]; then
    su - postgres -c "createdb org_live"
    su - postgres -c "psql org_live -c 'CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;'"

    mkdir ${INSTALLDIR}/${REPO}/media
    mkdir ${INSTALLDIR}/${REPO}/media/upload
    mkdir ${INSTALLDIR}/${REPO}/static

    chown -R ubuntu:ubuntu ${INSTALLDIR}/${REPO}/media
    chown -R ubuntu:ubuntu ${INSTALLDIR}/${REPO}/static

    $manage syncdb --noinput
    $manage migrate --noinput
    $manage collectstatic --noinput
    $manage loaddata ${INSTALLDIR}/${REPO}/org/fixtures/sites.json
    touch ${INSTALLDIR}/one-org-installed
else
    $manage migrate --noinput
    $manage collectstatic --noinput
fi

/etc/init.d/memcached restart

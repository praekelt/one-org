manage="${VENV}/bin/python ${INSTALLDIR}/${REPO}/manage.py"

$manage syncdb --noinput --no-initial-data
$manage migrate --noinput
$manage collectstatic --noinput

if [ ! -f ${INSTALLDIR}/one-org-installed ]; then
    $manage loaddata ${INSTALLDIR}/${REPO}/one/fixtures/sites.json
    touch ${INSTALLDIR}/one-org-installed
fi

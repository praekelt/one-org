from django.contrib.gis.utils import GeoIP


def get_country_code(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if not ip:
        return ''

    g = GeoIP()
    return g.country(ip)['country_code'] or 'ZA'
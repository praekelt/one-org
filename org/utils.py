from django.contrib.gis.utils import GeoIP
from django.core.validators import RegexValidator


validate_phone = RegexValidator(regex=r'^\d{9,15}$', message="Must be between 9 and 15 numerical values.")

validate_name = RegexValidator(regex=r'^[a-zA-Z]*$', message="Only alpha characters allowed.")

def get_country_code(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if not ip:
        return ''

    g = GeoIP()
    return g.country(ip)['country_code'] or ''
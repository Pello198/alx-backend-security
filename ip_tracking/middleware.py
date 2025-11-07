from django.http import HttpResponseForbidden
from django.core.cache import cache
from ipgeolocation import IpGeoLocationDatabase
from .models import RequestLog, BlockedIP
from django.http import HttpResponseForbidden
class RequestTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # determine IP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # block if exists
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Access denied")

        # ————— GEO LOCATION (cached for 24hrs = 86400sec) —————
        cache_key = f"geo_ip:{ip}"
        geo_data = cache.get(cache_key)

        if not geo_data:
            info = geo.lookup(ip) or {}
            country = info.get("country_name")
            city = info.get("city")

            geo_data = {"country": country, "city": city}
            cache.set(cache_key, geo_data, timeout=86400)  # 24 hours
        else:
            country = geo_data["country"]
            city = geo_data["city"]

        # save request log
        RequestLog.objects.create(
            ip_address=ip,
            path=request.path,
            country=country,
            city=city
        )

        return self.get_response(request)
class RequestTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get IP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Access denied")

        # create log record
        RequestLog.objects.create(
            ip_address=ip,
            path=request.path
        )

        return self.get_response(request)

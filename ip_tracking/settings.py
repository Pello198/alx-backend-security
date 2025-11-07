MIDDLEWARE = [
    ...
    'ip_tracking.middleware.RequestTrackingMiddleware',
]
RATELIMIT_RATES = {
    'user_or_ip': '10/m',
    'ip': '5/m',
}
INSTALLED_APPS = [
    ...
    'ratelimit',
]

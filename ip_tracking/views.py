from django.http import HttpResponse
from ratelimit.decorators import ratelimit

# anonymous users → 5 requests per minute
# authenticated users → 10 requests per minute

@ratelimit(key='ip', rate='10/m', method='POST', block=True)
def login_authenticated(request):
    return HttpResponse("Authenticated login attempt OK")

@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def login_anonymous(request):
    return HttpResponse("Anonymous login attempt OK")

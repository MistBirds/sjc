from sjc.admin import site
from django_ratelimit.decorators import ratelimit


@ratelimit(key='ip', rate='5/m', method=['GET', 'POST'], block=True)
def sjc_login(request):
    return site.login(request)

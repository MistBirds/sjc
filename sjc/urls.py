from django.contrib import admin
from django.urls import path, include
from sjc.views import sjc_login

urlpatterns = [
    path('admin/login/', sjc_login),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
]

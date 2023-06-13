from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User, Group

from sjc.forms import SjcAuthenticationForm


class SjcAdminSite(AdminSite):
    login_form = SjcAuthenticationForm


site = SjcAdminSite()
site.register(User)
site.register(Group)

from django.contrib.admin.apps import AdminConfig


class SjcAdminConfig(AdminConfig):
    default_site = "sjc.admin.SjcAdminSite"

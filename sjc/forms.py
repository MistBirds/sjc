from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from captcha.fields import CaptchaField


class SjcAuthenticationForm(AuthenticationForm):

    captcha = CaptchaField()

    error_messages = {
        **AuthenticationForm.error_messages,
        "invalid_login": _(
            "Please enter the correct %(username)s and password for a staff "
            "account. Note that both fields may be case-sensitive."
        ),
    }
    required_css_class = "required"

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_staff:
            raise ValidationError(
                self.error_messages["invalid_login"],
                code="invalid_login",
                params={"username": self.username_field.verbose_name},
            )

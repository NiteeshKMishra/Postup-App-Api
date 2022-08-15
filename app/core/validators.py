from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_dob(value):
    if value is not None:
        formatted_dob = datetime.strptime(str(value), "%Y-%m-%d")
        dob_year = formatted_dob.year
        valid_year = datetime.today().year - 12
        if int(dob_year) > valid_year:
            raise ValidationError(
                _(f"Year of birth should be less than or equal to {valid_year}"),
                params={'value': value})

"""
Custom django models.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from core.validators import validate_dob


class UserManager(BaseUserManager):
    """User manger for system users"""

    def create_user(self, email, password, **extra_fields):
        """Create and  returns user"""
        if email is None or email == "":
            raise ValueError("Email is required")
        if password is None or password == "":
            raise ValueError("Password is required")
        if "dob" in extra_fields:
            dob = extra_fields["dob"]
            validate_dob(dob)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return super user"""
        super_user = self.create_user(
            email=email, password=password
        )
        super_user.is_superuser = True
        super_user.is_staff = True
        super_user.save(using=self._db)

        return super_user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(
        max_length=255,
        unique=True,
        help_text="Email of user")
    name = models.CharField(max_length=255, help_text="Name of user")
    dob = models.DateField(null=True, validators=[validate_dob], help_text="Date of birth of user")
    is_active = models.BooleanField(
        default=True,
        help_text="User is active or not")
    is_staff = models.BooleanField(
        default=False,
        help_text="User is staff or not")

    objects = UserManager()

    USERNAME_FIELD = "email"

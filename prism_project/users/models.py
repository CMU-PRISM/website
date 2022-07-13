from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import int_list_validator

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(
            self, username, email, first_name, last_name, password=None,
            commit=True):
        """
        Creates and saves a User with the given email, first name, last name
        and password.
        """
        if not username:
            raise ValueError(_('Users must provide an andrew id or other username'))
        if not email:
            raise ValueError(_('Users must provide an email address'))
        if not first_name:
            raise ValueError(_('Users must provide a first name'))
        if not last_name:
            raise ValueError(_('Users must provide a last name'))

        user = self.model(
            username = username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            username   = username,
            email      = email,
            password   = password,
            first_name = first_name,
            last_name  = last_name,
            commit     = False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name = 'email address', max_length = 255, unique = True)
    # password field by AbstractBaseUser
    # last_login field by AbstractBaseUser
    first_name = models.CharField(_('first name'), max_length = 30, blank = True)
    last_name = models.CharField(_('last name'), max_length = 30, blank = True)
    username = models.CharField(_('username'), max_length = 30, blank = True)

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )
    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin

    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    
    def get_id(self):
        return '{}'.format(self.username)
    
    def get_first_name(self):
        """
        Return the first_name, capitalized and stripped.
        """
        return '{}'.format(self.first_name).capitalize().strip()
    
    def get_last_name(self):
        """
        Return the last_name, capitalized and stripped.
        """
        return '{}'.format(self.last_name).capitalize().strip()

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.get_first_name(), self.get_last_name())
        return full_name

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.email)
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    class Meta:
        permissions = (
            ('can_open', "Can mark room as open/closed"),
        )
        
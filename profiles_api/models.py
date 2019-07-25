from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# see model ref for this https://docs.djangoproject.com/en/1.11/ref/models/fields/


#customer user User manager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users Must Have an Email address")
        #normalize email address - make firs half case-insensitive
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) # this encrypts the password in the DB
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        """ CReate and save a new superuser with given details"""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

# using a custom model for user profile model

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

# define custom model manager

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ retrieve full name of user """
        return self.name


    def get_short_name(self):
        """ retrieve short name of user """
        return self.name


    def __str_(self):
        """  Return string rep of our user"""

        return self.email

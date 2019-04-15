from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework import status

# Create your models here.
import re


def validate_mobile_number(value):
    """
    Validates the mobile number to ascertain it's of nigerian format
    :param value: The mobile number to be validated
    :return: validation error if value is not of correct format
    """
    result = re.findall('[0][7,8,9][0-9]{9}', value)
    if not result:
        raise ValidationError('The number must be of nigerian mobile format', status.HTTP_400_BAD_REQUEST)


class DeveloperManager(BaseUserManager):

    def create_user(self, firstname, lastname, email, mobile, date_of_birth, password, **extra_fields):
        """
        Creates and saves a Developer(user) with the given firstname, lastname, email and date of birth
        """
        if not firstname:
            raise ValueError('Firstname field is required')

        if not lastname:
            raise ValueError('lastname field is required')

        if not email:
            raise ValueError('email field is required')

        if not mobile:
            raise ValueError('mobile field is required')

        if not date_of_birth:
            raise ValueError('date of birth field is required')

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            date_of_birth=date_of_birth,
            mobile=mobile,
            **extra_fields
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, firstname, lastname, mobile, password):
        """Creates and saves the Super User"""
        user = self.create_user(firstname, lastname, email, mobile, date_of_birth, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Developer(AbstractBaseUser):
    """This class implements the developer model"""
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    mobile = models.CharField(unique=True, max_length=11, validators=[validate_mobile_number])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    twitter = models.URLField(max_length=100)
    linkedin = models.URLField(max_length=100)
    facebook = models.URLField(max_length=100)
    github = models.URLField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = DeveloperManager()

    REQUIRED_FIELDS = ['firstname', 'lastname', 'date_of_birth', 'mobile']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_username(self):
        return self.email

    @property
    def is_staff(self):
        # Is the user a member or a staff?
        # Simplest possible answer: All admins are staff
        return self.is_admin
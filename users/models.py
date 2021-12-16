from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from core import managers as core_managers


class User(AbstractUser):
    
    """ Custom User Model """

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_USD = "krw"
    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_USD, "KRW"))

    LOGIN_KAKAO = "kakao"
    LOGIN_NAVER = "naver"
    LOGIN_GOOGLE = "google"
    LOGIN_CHOICES = (
        (LOGIN_KAKAO, "Kakao"),
        (LOGIN_NAVER, "Naver"),
        (LOGIN_GOOGLE, "Google"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    email_verified = models.BooleanField(default=False)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_KAKAO
    )
    objects = core_managers.CustomModelManager()

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
    
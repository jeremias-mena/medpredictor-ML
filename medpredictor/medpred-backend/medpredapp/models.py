from django.db import models

class UserDB(models.Model):
    user_name = models.CharField(verbose_name="User name", max_length=50, null=False, blank=False)
    first_name = models.CharField(verbose_name="First Name", max_length=75, null=False, blank=False)
    last_name = models.CharField(verbose_name="First Name", max_length=75, null=False, blank=False)
    birth_date = models.DateField(verbose_name="Birth date", null=False, blank=False)
    email = models.EmailField(verbose_name="Email", null=False, blank=False)


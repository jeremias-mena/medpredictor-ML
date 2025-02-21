from django.db import models

class UserDB(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=75, null=False, blank=False)
    last_name = models.CharField(verbose_name="First Name", max_length=75, null=False, blank=False)
    birth_date = models.DateField(verbose_name="Birth date", null=False, blank=False)
    email = models.EmailField(verbose_name="Email", null=False, blank=False)

class AnswersDB(models.Model):
    answers_yn = {'Yes': 'Yes',
                  'No': 'No'}
    answers_diab = {'No diabetes': 'No diabetes',
                    'Prediabetes': 'Pre diabetes',
                    'Diabetes': 'Diabetes'}
    diabetes = models.CharField(verbose_name='Diabetes', max_length=1, choices=answers_diab)
    heartattack = models.CharField(verbose_name='Heart attack', max_length=1, choices=answers_yn)
    stroke = models.CharField(verbose_name='Stroke', max_length=1, choices=answers_yn)
    veggie = models.CharField(verbose_name='Veggie', max_length=1, choices=answers_yn)
    fruits = models.CharField(verbose_name='Fruits', max_length=1, choices=answers_yn)
    smoker = models.CharField(verbose_name='Smoker', max_length=1, choices=answers_yn)
    alcohol = models.CharField(verbose_name='Heavy alcohol consume', max_length=1, choices=answers_yn) 

from django.db import models

class AnswersDB(models.Model):
    answers_yn = {'Yes': 'Yes',
                  'No': 'No'}
    answers_status = {'Excellent': 'Excellent',
                      'Very good': 'Very good',
                      'Good': 'Good',
                      'Fair': 'Fair',
                      'Poor': 'Poor'}
    bmi = models.FloatField(verbose_name="Body mass index", null=False, blank=False)
    veggie = models.CharField(verbose_name="Veggie", max_length=3, choices=answers_yn, null=False, blank=False)
    fruits = models.CharField(verbose_name="Fruits", max_length=3, choices=answers_yn, null=False, blank=False)
    smoker = models.CharField(verbose_name="Smoker", max_length=3, choices=answers_yn, null=False, blank=False)
    alcohol = models.CharField(verbose_name="Heavy alcohol consume", max_length=3, choices=answers_yn, null=False, blank=False) 
    highbp = models.CharField(verbose_name="High blood pressure", max_length=3, choices=answers_yn, null=False, blank=False)
    highchol = models.CharField(verbose_name="High cholesterol", max_length=3, choices=answers_yn, null=False, blank=False)
    diffwalk = models.CharField(verbose_name="Difficulty walking", max_length=3, choices=answers_yn, null=False, blank=False)
    physact = models.CharField(verbose_name="Physical activity", max_length=3, choices=answers_yn, null=False, blank=False)
    healtstatus = models.CharField(verbose_name="General health status", max_length=10, choices=answers_status, null=False, blank=False)

    class Meta:
        db_table = "Answers"
        verbose_name = "Answer"
        verbose_name_plural ="Answers"

class UserDB(models.Model):
    sex = {'Male': 'Male',
           'Female': 'Female'}
    first_name = models.CharField(verbose_name="First Name", max_length=75, null=False, blank=False)
    last_name = models.CharField(verbose_name="Last Name", max_length=75, null=False, blank=False)
    sex = models.CharField(verbose_name="Sex", max_length=10, choices=sex, null=False, blank=False)
    age = models.CharField(verbose_name="Age", max_length=10, null=False, blank=False)
    birth_date = models.DateField(verbose_name="Birth date", null=False, blank=False)
    email = models.EmailField(verbose_name="Email", null=False, blank=False)
    form_answers = models.ForeignKey(AnswersDB, on_delete=models.CASCADE)

    class Meta:
        db_table = "Users"
        verbose_name = "User"
        verbose_name_plural ="Users"
    
    def __str__(self) -> str:
        return self.first_name
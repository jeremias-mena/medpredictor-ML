from django.shortcuts import render, redirect
from django.views import View
from medpredapp.models import UserDB, AnswersDB

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class UserFormView(View):
    def get(self, request):
        return render(request, 'user_form.html')
    
    def transform_age(self, age):
        if age >= 18 and age <= 24:
            return '18 to 24'
        elif age > 24 and age <= 29:
            return '25 to 29'
        elif age > 29 and age <= 34:
            return '30 to 34'
        elif age > 34 and age <= 39:
            return '35 to 39'
        elif age > 39 and age <= 44:
            return '40 to 44'
        elif age > 44 and age <= 49:
            return '45 to 49'
        elif age > 50 and age <= 54:
            return '50 to 54'
        elif age > 54 and age <= 59:
            return '55 to 59'
        elif age > 59 and age <= 64:
            return '60 to 64'
        elif age > 64 and age <= 69:
            return '65 to 69'
        elif age > 69 and age <= 74:
            return '70 to 74'
        elif age > 74 and age <= 79:
            return '75 to 79'
        else:
            return '80 or older'

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        sex = request.POST.get('sex')
        age_input = request.POST.get('age')

        if age_input: 
            age = UserFormView().transform_age(int(age_input))
        else:
            age = None

        email = request.POST.get('email')
        birth_date = request.POST.get('birth_date')

        if first_name and last_name and sex and age and birth_date and email:
            user = UserDB.objects.create(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                age=age,
                birth_date=birth_date,
                email=email,
                form_answers = None
            )
            user.save()
            return redirect('register_answers')

        return render(request, 'user_form.html', {'error': 'All fields are required'})


class QuestionFormView(View):
    def get(self, request):
        return render(request, 'question_form.html')
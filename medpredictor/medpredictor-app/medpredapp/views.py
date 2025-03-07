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
        if request.method == 'POST':
            first_name= request.POST.get('first_name', 'undefined')
            last_name = request.POST.get('last_name', 'undefined')
            sex = request.POST.get('sex', 'undefined')
            age_input = request.POST.get('age')

            if age_input: 
                age = self.transform_age(int(age_input))
            else:
                age = None

            email = request.POST.get('email', 'undefined')
            birth_date = request.POST.get('birth_date', 'undefined')

            if first_name and last_name and sex and age and email and birth_date:
                request.session['user_data'] = {'first_name':first_name,
                                                'last_name':last_name,
                                                'sex':sex,
                                                'age':age,
                                                'birth_date':birth_date,
                                                'email':email
                                                }
                request.session.modified = True
                request.session.save()
                return redirect('register_answers')

        return render(request, 'user_form.html', {'error': 'All fields are required'})

class QuestionFormView(View):
    def get(self, request):
        return render(request, 'question_form.html')
    
    def post(self, request):
        if request.method == 'POST':
            bmi = request.POST.get('bmi', 'undefined')
            veggie = request.POST.get('veggie', 'undefined')
            fruits = request.POST.get('fruits', 'undefined')
            smoker = request.POST.get('smoker', 'undefined')
            alcohol = request.POST.get('alcohol', 'undefined')
            highbp = request.POST.get('highbp', 'undefined')
            highchol = request.POST.get('highchol', 'undefined')
            diffwalk = request.POST.get('diffwalk', 'undefined')
            physact = request.POST.get('physact', 'undefined')
            healtstatus = request.POST.get('healtstatus', 'undefined')

            if bmi and veggie and fruits and smoker and alcohol and highbp and highchol and diffwalk and physact and healtstatus:
                request.session['answers_data'] = {'bmi':bmi,
                                                   'veggie':veggie,
                                                   'fruits':fruits,
                                                   'smoker':smoker,
                                                   'alcohol':alcohol,
                                                   'highbp':highbp,
                                                   'highchol':highchol,
                                                   'diffwalk':diffwalk,
                                                   'physact':physact,
                                                   'healtstatus':healtstatus}
                request.session.modified = True
                request.session.save()
                return redirect('save_data')
        return render(request, 'question_form.html', {'error': 'All fields are required'})
    
class SaveDataView(View):
    def get(self, request):
         user_data = request.session.get('user_data')
         answers_data = request.session.get('answers_data')

         if not user_data or not answers_data:
            return render(request, 'error_registration.html', {'error':"There's no data to load"})
            
         try:
                answers = AnswersDB.objects.create(bmi=answers_data['bmi'],
                                                   veggie=answers_data['veggie'],
                                                   fruits=answers_data['fruits'],
                                                   smoker=answers_data['smoker'],
                                                   alcohol=answers_data['alcohol'],
                                                   highbp=answers_data['highbp'],
                                                   highchol=answers_data['highchol'],
                                                   diffwalk=answers_data['diffwalk'],
                                                   physact=answers_data['physact'],
                                                   healtstatus=answers_data['healtstatus'])

                UserDB.objects.create(first_name=user_data['first_name'],
                                             last_name=user_data['last_name'],
                                             sex=user_data['sex'],
                                             age=user_data['age'],
                                             birth_date=user_data['birth_date'],
                                             email=user_data['email'],
                                             form_answers=answers
                                             )

                return render(request, 'successfull_registration.html')
            
         except Exception as e:
            return render(request, 'error_registration.html', {'error':f"Error when saving in the data base {str(e)}"})

        
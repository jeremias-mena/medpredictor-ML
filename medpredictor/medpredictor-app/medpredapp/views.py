from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class UserFormView(View):
    def get(self, request):
        return render(request, 'user_form.html')

class QuestionFormView(View):
    def get(self, request):
        return render(request, 'question_form.html')
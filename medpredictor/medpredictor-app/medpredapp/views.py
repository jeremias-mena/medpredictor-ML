from django.shortcuts import render

def HomeView(request):
    return render(request, "home.html")

def UserFormView (request):
    return render(request, "user_form.html")

def QuestionFormView(request):
    return render(request, "question_form.html")

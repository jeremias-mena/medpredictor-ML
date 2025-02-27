from django.contrib import admin
from django.urls import path
from medpredapp.views import HomeView, UserFormView, QuestionFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/home', HomeView),
    path('/registeruser', UserFormView),
    path('/registeranswers', QuestionFormView)
]

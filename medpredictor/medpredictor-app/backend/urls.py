from django.contrib import admin
from django.urls import path
from medpredapp.views import HomeView, UserFormView, QuestionFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('registeruser', UserFormView.as_view(), name='register_user'),
    path('registeranswers', QuestionFormView.as_view(), name='register_answers')
]

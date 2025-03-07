from django.contrib import admin
from django.urls import path
from medpredapp.views import HomeView, UserFormView, QuestionFormView, SaveDataView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('registeruser', UserFormView.as_view(), name='register_user'),
    path('registeranswers', QuestionFormView.as_view(), name='register_answers'),
    path('save-data', SaveDataView.as_view(), name='save_data')
]

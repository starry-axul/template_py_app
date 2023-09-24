from django.urls import path
from .views import *

app_name = 'templates'

urlpatterns = [
    path("", Templates.as_view()),
    path('<int:id>', Templates_Detail.as_view()),
]
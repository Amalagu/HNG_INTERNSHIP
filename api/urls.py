from django.urls import path
from .views import person_api
urlpatterns = [
    path('api/', person_api, name='api'),
]
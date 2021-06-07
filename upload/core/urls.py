from django.urls import path
from .views import video

urlpatterns = [
    path('', video)
]

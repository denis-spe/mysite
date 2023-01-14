from django.urls import path
from . import views

# Create urls patterns.
urlpatterns = [
            path('', view=views.index, name='index')
        ]

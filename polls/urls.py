from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
        # ex: /polls/
        path("", view=views.index, name="index"),

        # ex: /polls/5
        path("<int:pk>/", view=views.detail,
             name="detail"),

        # ex: /polls/5/results/
        path(
            "<int:pk>/results/", 
            view=views.results,
            name="results"),

        # ex: /polls/5/vote/
        path(
            "<int:question_id>/vote/", 
            view=views.vote,
             name="vote"),

        ]

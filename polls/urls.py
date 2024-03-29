from django.urls import path
from . import views

urlpatterns = [
        # ex: /polls/
        path("", view=views.index, name="index"),

        # ex: /polls/5
        path("<int:question_id>/", view=views.detail,
             name="detail"),

        # ex: /polls/5/results/
        path(
            "<int:question_id>/results/", 
            view=views.results,
            name="results"),

        # ex: /polls/5/vote/
        path(
            "<int:question_id>/vote/", 
            view=views.vote,
             name="vote"),

        ]

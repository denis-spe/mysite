from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.db.models import F
from django.views import generic

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return last five published question
        """
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


"""
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    #template = loader.get_template("polls/index.html")   
    # Use the shortcut
    context = {
            "latest_question_list": 
            latest_question_list
            }
    return render(request, "polls/index.html", context)

    #return HttpResponse(
    #template.render(context, request))


def detail(request, question_id):
    #try:
        #question = Question.objects.get(
                #pk=question_id)
    #except Question.DoesNotExist:
        #raise Http404("Question does not exist")
    question = get_object_or_404(
            Question, pk=question_id)

    return render(
            request,
            "polls/detail.html", 
            {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question,
                    pk=question_id)
    return render(request,
                  "polls/results.html",
                  {"question": question})
"""

def vote(request, question_id):
    # Get the object or raise a 404 error
    question = get_object_or_404(Question,
                    pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, {
            "question": question,
            "error_message": "You didn't select a choice"
            })
    else:
        selected_choice.vote = F("vote") + 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



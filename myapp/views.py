# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
# from .models import Question
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from account.models import Account

# def index(request):
#     return HttpResponse("Hello, Django. You're at the polls index.")

# from django.http import HttpResponse

def home_screen_view(request):
    print(request.headers)

    # context = {
    # "variable": "value"
    # }      

    context = {}
    # context["variable"] = "value's"

    # list_of_values = [1,2,3,4,5]
    # context["list_of_values"] = list_of_values

    account = Account.objects.all()
    context["account"] = account

    
    return render(request, "polls/home.html", context)


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # template = loader.get_template("polls/index.html")
#     # context = {"latest_question_list": latest_question_list}
#     # return HttpResponse(template.render(context, request))
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)
 
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


from django.shortcuts import render, get_object_or_404,redirect
from .models import Question, Choice
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def index(request):
    questions=Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    return render(request, 'index.html',{'questions':questions})


def vote(request, id):
    question=get_object_or_404(Question, pk=id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        context={
        'question':question,
        'error_message':"You didn't select a Choice !!!",
    }
        return render(request, 'detail_page.html',context)
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return redirect(reverse("vote:result", args=(question.id,)))
    
    
class ResultView(DetailView):
    model=Question
    template_name='results.html'

    

@login_required
def detail(request,id):
    question=get_object_or_404(Question, pk=id)
    context={
        'question':question,
    }
    return render(request, 'detail_page.html', context)
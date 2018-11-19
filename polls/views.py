from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice,Comments
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import QuestionForm,CommentForm
from django.contrib.auth.models import User

# Create your views here.
class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:]

import os
def detailview(request,pk):
    question = get_object_or_404(Question, id=pk)
    comment = Comments.objects.filter(question=question)


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if (form.is_valid()):
            # form.save()
            auth = request.user
            comments = form.cleaned_data.get('comment')
            question = question
            obj=Comments(auth=auth,comment=comments,question=question)
            obj.save()
            request.method='GET'
            return redirect(os.path.join('/polls/',str(pk)))
        else:
            print('form is not valid')
    else:
        form = CommentForm()

    context={'question':question,'comment':comment,'form': form}
    template_name = 'polls/detail.html'
    # question=question.question
    return render(request,template_name,context)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    comment = Comments.objects.filter(question=question)
    if (request.user.is_authenticated):
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice']) #choice_set is the related manager used
        except (KeyError, Choice.DoesNotExist):                                  # to access objects of the related tables
                                                                                 # here access choice table by question table object
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
                'comment':comment,
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    else:
        return redirect('/login/')
def search(request):
    template= 'polls/index.html'
    query=request.GET.get('q')
    if query:
        results = Question.objects.filter(Q(question__icontains=query))
    else:
        results = Question.objects.filter(order_by='pub_date')
    context ={
    'latest_question_list': results,
    }
    return render(request,template,context)

# signup and login page view

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/polls/')
    else:
        form = UserCreationForm()
    return render(request, 'polls/signup.html', {'form': form})

def new_poll(request):
    template='polls/post.html'
    if request.method == 'POST':
        form = QuestionForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            auth=request.user
            question=form.cleaned_data['question']
            choice_1=form.cleaned_data['choice_1']
            choice_2=form.cleaned_data['choice_2']
            choice_3=form.cleaned_data['choice_3']
            choice_4=form.cleaned_data['choice_4']
            choice_5=form.cleaned_data['choice_5']
            choice_6=form.cleaned_data['choice_6']
            choice_7=form.cleaned_data['choice_7']
            choice_8=form.cleaned_data['choice_8']

            try:
                image=form.files['image']
            except:
                image='empty.png'
            obj=Question(auth=auth,question=question,image=image)
            obj.save()
            list=[choice_1,choice_2,choice_3,choice_4,choice_5,choice_6,choice_7,choice_8]
            for choice in list:
                if choice:
                    obj_choice=Choice(question=obj,choice_text=choice)
                    obj_choice.save()
            return redirect('/polls/')

        else:
            form = QuestionForm()
    else:
        form = QuestionForm()
    context = {
        'form':form,
    }
    return render(request,template,context)

def yourPolls(request):
    template= 'polls/index.html'
    query=request.user
    result=Question.objects.filter(auth=query)

    context ={
    'latest_question_list': result,
    }
    return render(request,template,context)

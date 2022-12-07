import datetime

from django.shortcuts import render
from f_app.models import  questions
from f_app.forms import examForms

# Create your views here.
def index(request):
    question=questions.objects.all()
    return render(request,'index.html',{"questions":question})

def about(request):
    return render(request,'about.html',{'Name':'RAGT'})

def exam(request):
    message=""

    if request.method=="POST":
        form=examForms()
        if bool(request.POST['question']) & bool(request.POST['answer']):
            form=examForms(request.POST)
            if form.is_valid():
                question = questions(question=form.cleaned_data['question'],answer=form.cleaned_data['answer'],date=datetime.datetime.now())
                # question = questions(question=request.POST['question'],answer=request.POST['answer'],date=datetime.datetime.now())
                question.save()
                message="Add succesfully"
            else:
                message = "Error vaildate"
        else:
            message="error check"
    else:
        message=datetime.datetime.now()

    return render(request,'exam.html',{'message':message,"examForm":examForms})
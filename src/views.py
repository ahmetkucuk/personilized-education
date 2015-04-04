from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.views.generic import FormView
from src.forms import *


def MainPage(request):
    return render_to_response(template_name='home.html')


def CrispyView(request):
    template_name='crispy.html'
    form_class = SampleForm()
    return render(request, "crispy.html", {'form': form_class})


def ContextView(request):
    if request.method == 'POST':
        #we need to create new student in each login
        student = Student(name="ahmet")
        student.save()
        #this initialization is done for passing required fields to ContextForm
        context = Context(user=student)
        form = ContextForm(request.POST, instance=context)
        if form.is_valid():
            form.save()
            redirect('/crispy')
    template_name='crispy.html'
    form_class = ContextForm()
    return render(request, "crispy.html", {'form': form_class})

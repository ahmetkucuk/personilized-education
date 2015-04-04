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
        student = Student.objects.get(pk=request.session["student_id"])
        #this initialization is done for passing required fields to ContextForm
        context = Context(user=student)
        form = ContextForm(request.POST, instance=context)
        if form.is_valid():
            form.save()
            print("form saved " + request.session['session_id'])
            return redirect('/preTest')

    student = Student(name="anonym") #create anonym student
    student.save()
    request.session['session_id'] = "23434"
    request.session['student_id'] = student.id
    request.session['treatment_id'] = 1 # choose random treatment, or ML
    template_name='crispy.html'
    form_class = ContextForm()
    return render(request, template_name, {'form': form_class})

def LessonView(request, lesson_number):
    if request.method == 'POST':
        if int(lesson_number) == 3:
            return redirect('/postTest')
        return redirect('/lesson/' + str(int(lesson_number) + 1))
    template_name='lesson.html'
    form_class = LessonForm()
    return render(request, template_name, {'form': form_class})

def PostTestView(request):
    if request.method == 'POST':
        return redirect('/')
    template_name='test.html'
    form_class = TestForm()
    return render(request, template_name, {'form': form_class})

def PreTestView(request):
    if request.method == 'POST':
        return redirect('/lesson/1')
    template_name='test.html'
    form_class = TestForm()
    return render(request, template_name, {'form': form_class})


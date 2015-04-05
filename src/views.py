from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.views.generic import FormView
from random import randint
from Utils import getLabel
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
            context = form.save()
            l = getLabel(context)
            student.label = Label.objects.get(label=l)
            student.save()
            print("form saved " + request.session['session_id'])
            return redirect('/preTest')

    student = Student(name="anonym") #create anonym student
    student.save()
    request.session['session_id'] = "23434"
    request.session['student_id'] = student.id
    #treatments = Treatment.objects.all()
    #treatment = treatments[randint(1, treatments.count())]
    treatment = Treatment.objects.get(pk=1)
    request.session['treatment_id'] = treatment.id # choose random treatment, or ML
    template_name='crispy.html'
    form_class = ContextForm()
    return render(request, template_name, {'form': form_class})

def LessonView(request, treatment_id, lesson_order):
    if request.method == 'POST':
        given_answer = request.POST['answer']
        student_id = request.session['student_id']
        student = Student.objects.get(pk=student_id)
        treatment = Treatment.objects.get(pk=treatment_id)
        lesson = getLesson(treatment, int(lesson_order))
        lesson_student = LessonStudent(student=student, treatment=treatment, lesson=lesson, given_answer=int(given_answer))
        lesson_student.save()
        if int(lesson_order) == 3:
            return redirect('/postTest')
        return redirect('/treatment/' + str(treatment_id) + '/lesson/' + str(int(lesson_order) + 1))
    template_name='lesson.html'
    treatment_id = request.session['treatment_id']

    treatment = Treatment.objects.get(pk=treatment_id)
    lesson = getLesson(treatment, int(lesson_order))
    form_class = LessonForm(lesson)
    return render(request, template_name, {'question_text': lesson.text, 'form': form_class})

def PostTestView(request):
    if request.method == 'POST':
        return redirect('/')
    template_name='test.html'
    form_class = TestForm()
    return render(request, template_name, {'form': form_class})

def PreTestView(request):
    if request.method == 'POST':
        return redirect('/treatment/' + str(request.session['treatment_id']) + '/lesson/1')
    template_name='test.html'
    form_class = TestForm()
    return render(request, template_name, {'form': form_class})

def getLesson(treatment, lesson_order):
    if lesson_order == 1:
        return treatment.lesson1
    if lesson_order == 2:
        return treatment.lesson2
    if lesson_order == 3:
        return treatment.lesson3
    return treatment.lesson1


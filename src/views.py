from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.views.generic import FormView
from src.forms import SampleForm


def MainPage(request):
    return render_to_response(template_name='home.html')


def CrispyView(request):
    template_name='crispy.html'
    form_class = SampleForm()
    return render(request, "crispy.html", {'form': form_class})

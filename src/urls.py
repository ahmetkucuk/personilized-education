from django.conf.urls import patterns, url
from src import views

urlpatterns = patterns( '',
	url( r'^$', views.MainPage, name = 'main'),
	url( r'crispy', views.CrispyView, name = 'crispy'),
)
from django.conf.urls import patterns, url
from src import views

urlpatterns = patterns( '',
	url( r'^$', views.MainPage, name = 'main'),
	url( r'crispy', views.CrispyView, name = 'crispy'),
	url( r'context', views.ContextView, name = 'context'),
	url( r'postTest', views.PostTestView, name = 'postTest'),
	url( r'preTest', views.PreTestView, name = 'preTest'),
	url( r'treatment/(?P<treatment_id>\d+)/lesson/(?P<lesson_order>\d+)', views.LessonView, name = 'lesson'),
)

from django.conf.urls import url, include
from . import views

app_name = 'website'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.RegisterUserView.as_view(), name='register'),
	url(r'^login/$', views.LoginUserView.as_view(), name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^student/$', views.student_view, name='student'),
	url(r'^teacher/$', views.teacher_view, name='teacher'),
	url(r'^feedback/$', views.FeedbackView, name='feedback'),
	# url(r'^student/performance/$', views.performance_view, name='performance'),
	# url(r'^student/feedback/$', views.feedback_view, name='feedback'),
	# url(r'^student/material/$', views.material_view, name='material'),
]
from django.conf.urls import url, include
from . import views

app_name = 'website'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.RegisterUserView.as_view(), name='register'),
	url(r'^login/$', views.LoginUserView.as_view(), name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
]
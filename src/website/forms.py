from django.contrib.auth.models import User
from .models import Feedback,Course
from django import forms

CHOICES=[('student','Student'),
         ('teacher','Teacher')]


class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	designation = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password', 'designation']

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'password']

class FeedbackForm(forms.ModelForm):
	course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label=None, to_field_name='course_code')
	class Meta:
		model = Feedback
		fields = ['course','feedback']
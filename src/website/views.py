from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render, redirect
from django.views.generic import View 
from .forms import RegisterForm, LoginForm, FeedbackForm
from .models import UserProfile, StudentMarks, Feedback, Course
from django.urls import reverse

# Create your views here.
def index(request):
	return render(request, 'website/index.html')

def logout_view(request):
	logout(request)
	return redirect('website:index')

def student_view(request):
	form = FeedbackForm(None)
	if request.user.is_authenticated():
		return render(request, 'website/student_profile.html', {'marks': StudentMarks.objects.get(name=request.user.first_name),'form': form})
	else:
		return redirect('website:login')

def teacher_view(request):
	if request.user.is_authenticated():
		return render(request, 'website/teacher_profile.html', {'students': StudentMarks.objects.all(), 'feedbacks': Feedback.objects.filter(course=Course.objects.get(instructor=request.user.username))})
	else:
		return redirect('website:login')		

class RegisterUserView(View):
	form_class = RegisterForm
	template_name = 'website/registration_form.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			# does not save to database, just creates form object
			user = form.save(commit=False)

			# cleaned, normalized data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns User objects if credentials are correct
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					designation = form.cleaned_data['designation']
					# to use user details on page
					# request.user.username , request.user.designation , etc.
					if designation == 'student':
						return redirect(reverse('website:student'))
					else:
						return redirect('website:teacher')

		return render(request, self.template_name, {'form': form})

class LoginUserView(View):
	form_class = LoginForm
	template_name = 'website/login_form.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# process form data
	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:

			login(request, user)

			if user.user.designation == 'student':
				return redirect(reverse('website:student'))
			else:
				return redirect(reverse('website:teacher'))

		else:

			return redirect('website:login')


def FeedbackView(request):
	if request.method == 'POST':		
		form = FeedbackForm(request.POST)
		if form.is_valid():
			# does not save to database, just creates form object
			feedback = form.save(commit=False)
			feedback.student = UserProfile.objects.get(user=request.user)
			feedback.save()
	return redirect('website:student')
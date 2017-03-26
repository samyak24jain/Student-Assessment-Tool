from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
	designation = models.CharField(default='', blank=True, max_length=50)

	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name + ' : ' + self.designation

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()

post_save.connect(create_profile, sender=User)			

class StudentMarks(models.Model):
	rollNo = models.CharField(max_length=10) #Student's Roll Number
	# student = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=User())
	name = models.CharField(max_length=50, default='')
	mq1 = models.IntegerField() #Midsem Question 1
	mq2 = models.IntegerField() #Midsem Question 2
	mq3 = models.IntegerField() #Midsem Question 3
	mlq = models.IntegerField() #Midsem Lab Question
	eq1 = models.IntegerField() #Endsem Question 1
	eq2 = models.IntegerField() #Endsem Question 2
	eq3 = models.IntegerField() #Endsem Question 3
	eq4 = models.IntegerField() #Endsem Question 4
	elq = models.IntegerField() #Endsem Lab Question
	assignment = models.FloatField() #Assignment
	project = models.FloatField() #Project
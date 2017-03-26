from django.contrib import admin
from django.contrib.auth.models import User
from .models import StudentMarks, UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('username', 'first_name', 'last_name', 'email', 'designation')

	def username(self, obj):
		return obj.user.username

	def first_name(self, obj):
		return obj.user.first_name

	def last_name(self, obj):
		return obj.user.last_name

	def email(self, obj):
		return obj.user.email

# class UserProfileInline(admin.StackedInline):
# 	model = UserProfile
# 	list_display = ('designation')

# class UserAdmin(admin.ModelAdmin):
#     inlines = (UserProfileInline,)
#     list_display = ('username', 'first_name', 'last_name', 'email', 'designation')

#     def designation(self, obj):
#     	return obj.email
    

class StudentMarksAdmin(admin.ModelAdmin):
	list_display = ('rollNo', 'name', 'mq1', 'mq2', 'mq3', 'mlq', 'eq1', 'eq2', 'eq3', 'eq4', 'elq', 'assignment', 'project')

# admin.site.unregister(User)
admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(User, UserAdmin)
admin.site.register(StudentMarks, StudentMarksAdmin)
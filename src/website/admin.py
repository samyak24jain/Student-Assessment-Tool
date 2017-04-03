from django.contrib import admin
from django.contrib.auth.models import User
from .models import StudentMarks, UserProfile, Department, Course, Feedback
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

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('dept_name','hod','num_of_labs')

class CourseAdmin(admin.ModelAdmin):
	list_display = ('course_code','course_name','dept_name', 'instructor')

	def dept_name(self, obj):
		return obj.dept.dept_name

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('course', 'feedback', 'student')

	def course(self, obj):
		return obj.course.course_code + ':' + obj.course.course_name

	def student(self, obj):
		return obj.student.user.first_name + ' ' + obj.student.user.last_name

# admin.site.unregister(User)
admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(User, UserAdmin)
admin.site.register(StudentMarks, StudentMarksAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Feedback, FeedbackAdmin)
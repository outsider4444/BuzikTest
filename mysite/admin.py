from django.contrib import admin

# Register your models here.
from mysite.models import Users, Groups, Courses, Articles, Themes, Marks, MaxStudentScore

admin.site.register(Users)
admin.site.register(Groups)
admin.site.register(Courses)
admin.site.register(Articles)
admin.site.register(Themes)
admin.site.register(Marks)
admin.site.register(MaxStudentScore)
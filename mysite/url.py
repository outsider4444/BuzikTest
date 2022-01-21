from django.urls import path, include

from . import views
urlpatterns = [
    path('articles/<int:pk>_download', views.article_download, name="articlesDownload"),

    path('students/<int:pk>/update', views.StudentsUpdate.as_view(), name='usersUpdate'),
    path('articles/<int:pk>/update', views.ArticlesUpdate.as_view(), name='articlesUpdate'),

    path('students/<int:pk>/delete', views.StudentsDelete.as_view(), name='usersDelete'),
    path('articles/<int:pk>/delete', views.ArticlesDelete.as_view(), name='articlesDelete'),

    path('marks/create', views.marksCreate, name='marksCreate'),
    path('students/create', views.StudentsCreate.as_view(), name='usersCreate'),
    path('courses/create', views.CoursesCreate.as_view(), name='coursesCreate'),
    path('groups/create', views.GroupsCreate.as_view(), name='groupsCreate'),
    path('articles/create', views.ArticlesCreate.as_view(), name='articlesCreate'),

    path('students/', views.StudentsList.as_view(), name='usersList'),
    path('marks/', views.marksList, name='marksList'),
    path('courses/', views.CoursesList.as_view(), name='coursesList'),
    path('groups/', views.GroupsList.as_view(), name='groupsList'),
    path('articles/', views.ArticlesList.as_view(), name='articlesList'),
    path('', views.main, name='mainPage')
]
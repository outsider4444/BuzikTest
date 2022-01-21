from django.http import FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
from mysite.forms import CreateMarksForm, CreateMaxScoreForm
from mysite.models import Users, Courses, Groups, Articles, Marks, Themes, MaxStudentScore


def main(request):
    """Главная страница"""
    return render(request, "main.html")


# Ученики
class StudentsList(ListView):
    """Список учеников"""
    model = Users
    template_name = "students/List.html"


class StudentsCreate(SuccessMessageMixin, CreateView):
    """Создание ученика"""
    model = Users
    fields = ['name', 'surname', 'second_name', 'group', 'email', 'password1', 'password2']
    template_name = "students/Create.html"
    success_url = '/students/'
    success_message = "Студент %(surname)s %(name)s был успешно создан"


class StudentsUpdate(SuccessMessageMixin, UpdateView):
    """Редактирование ученика"""
    model = Users
    fields = ['name', 'surname', 'second_name', 'group', 'email', 'password1', 'password2']
    template_name = "students/Create.html"
    success_url = '/students/'
    success_message = "Студент %(surname)s %(name)s был успешно изменен"


class StudentsDelete(SuccessMessageMixin, DeleteView):
    """Удалить ученика"""
    model = Users
    fields = ['name', 'surname', 'second_name', 'group', 'email', 'password1', 'password2']
    template_name = "students/Delete.html"
    success_url = '/students/'
    success_message = "Студент был успешно удален"


# Курсы
class CoursesList(ListView):
    """Список курсов"""
    model = Courses
    template_name = "courses/List.html"


class CoursesCreate(CreateView):
    """Создание курса"""
    model = Courses
    fields = ['name']
    template_name = "courses/Create.html"
    success_url = '/courses/'
    success_message = "Курс %(name)s был успешно создан"


# Группы
class GroupsList(ListView):
    """Список групп"""
    model = Groups
    template_name = "groups/List.html"


class GroupsCreate(CreateView):
    """Создание группы"""
    model = Groups
    fields = ['name', 'specialize', 'course']
    template_name = "groups/Create.html"
    success_url = '/groups/'
    success_message = "Группа %(name)s была успешно создана"


# Оценки
def marksList(request):
    """Список оценок"""
    themes_list = Themes.objects.all()
    marks_list = Marks.objects.all()
    students_list = Users.objects.all()
    max_score_list = MaxStudentScore.objects.all()

    context = {"marks_list": marks_list, "themes_list": themes_list, 'students_list': students_list,
               'max_score_list': max_score_list}
    return render(request, "marks/List.html", context)


def marksCreate(request):
    """Добавление оценки"""
    themes_list = Themes.objects.all()
    marks_list = Marks.objects.all()
    students_list = Users.objects.all()
    form1 = CreateMarksForm()
    ball = 0

    if request.method == "POST":
        form1 = CreateMarksForm(request.POST)
        if form1.is_valid():
            # Берем id студента и тему по которой выставляется оценка
            user_id = form1.cleaned_data.get('user')
            theme_id = form1.cleaned_data.get('theme')

            # Ищем и удаляем все предыдущие оценки, если случайно выставляется в эту же графу
            new_score = Marks.objects.filter(user=user_id, theme=theme_id)
            new_score.delete()
            # Добавляется новая оценка
            form1.save()
            # Подсчёт суммы с учётом новой оценки
            for student in students_list:
                for mark in marks_list:
                    if mark.user == user_id & mark.user.id == student.id:
                        ball += mark.mark

            # Удаление предыдущего результата
            pred_score = MaxStudentScore.objects.filter(user=user_id)
            if pred_score.exists():
                pred_score.delete()
            # Выставление новой оценки
            MaxStudentScore.objects.update_or_create(user=user_id, max_ball=ball)
            return redirect(reverse('marksList'))
        else:
            # поставить потом заглушку - ошибки
            pass

    context = {"marks_list": marks_list, "themes_list": themes_list, 'students_list': students_list,
               'form1': form1,}
    return render(request, "marks/Create.html", context)


# Статьи
class ArticlesList(ListView):
    """Список статей"""
    model = Articles
    template_name = "articles/List.html"


class ArticlesCreate(CreateView):
    """Создание статьи"""
    model = Articles
    fields = ['name', 'file']
    template_name = "articles/Create.html"
    success_url = '/articles/'
    success_message = "Статья %(name)s была успешно создана"


class ArticlesUpdate(SuccessMessageMixin, UpdateView):
    """Редактирование статьи"""
    model = Articles
    fields = ['name', 'file']
    template_name = "articles/Create.html"
    success_url = '/articles/'
    success_message = "Статья %(name)s был успешно изменена"


class ArticlesDelete(SuccessMessageMixin, DeleteView):
    """Удалить статьи"""
    model = Articles
    fields = ['name', 'file']
    template_name = "articles/Delete.html"
    success_url = '/articles/'
    success_message = "Статья была успешно удалена"


def article_download(request, pk):
    obj = Articles.objects.get(id=pk)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response

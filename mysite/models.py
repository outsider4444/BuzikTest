from django.db import models

# Create your models here.


class Themes(models.Model):
    """Темы работ"""
    name = models.CharField('Название', max_length=225)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = 'Темы'


class Courses(models.Model):
    """Курсы"""
    name = models.CharField('Курс', max_length=225)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = 'Курсы'


class Groups(models.Model):
    """Группы"""
    name = models.CharField('Название группы', max_length=225)
    specialize = models.CharField('Специальность', max_length=225)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='Course', verbose_name='Курс')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = 'Группы'


class Users(models.Model):
    """Пользователи"""
    surname = models.CharField('Фамилия', max_length=225)
    name = models.CharField('Имя', max_length=225)
    second_name = models.CharField('Отчество', max_length=225)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name='Group', verbose_name="Группа")
    email = models.EmailField('Почта', max_length=100, unique=True)
    password1 = models.CharField('Пароль1', max_length=100)
    password2 = models.CharField('Пароль2', max_length=100)

    def __str__(self):
        return str(self.name + ' ' + self.surname)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'


class Marks(models.Model):
    """Оценки"""
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='User', verbose_name="Студент")
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE, related_name='Theme', verbose_name="Тема")
    mark = models.IntegerField('Оценка', null=True)

    def __str__(self):
        return str(self.mark)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = 'Оценки'


class MaxStudentScore(models.Model):
    """Максимальный балл"""
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='UserScore', verbose_name="Студент", null=True)
    max_ball = models.IntegerField('Максимальный балл', null=True)

    def __str__(self):
        return str(self.max_ball)

    class Meta:
        verbose_name = "Максимальная оценка"
        verbose_name_plural = 'Максимальные оценки'


class Articles(models.Model):
    """Файлы"""
    name = models.CharField('Название статьи', max_length=225)
    file = models.FileField('Файл', upload_to='articles/')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = 'Статьи'


class UsefulLinks(models.Model):
    """Полезные ссылки"""
    name = models.CharField('Название статьи', max_length=225)
    link = models.CharField('Ссылка', max_length=225)
    desciption = models.CharField('Описание', max_length=225)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = 'Ссылки'
# Generated by Django 4.0.1 on 2022-01-20 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Название статьи')),
                ('file', models.FileField(upload_to='articles/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Название группы')),
                ('specialize', models.CharField(max_length=225, verbose_name='Специальность')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Course', to='mysite.courses', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=225, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=225, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=225, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Почта')),
                ('password1', models.CharField(max_length=100, verbose_name='Пароль1')),
                ('password2', models.CharField(max_length=100, verbose_name='Пароль2')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Group', to='mysite.groups', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='MaxStudentScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_ball', models.IntegerField(null=True, verbose_name='Максимальный балл')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserScore', to='mysite.users', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Максимальная оценка',
                'verbose_name_plural': 'Максимальные оценки',
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(null=True, verbose_name='Оценка')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Theme', to='mysite.themes', verbose_name='Тема')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to='mysite.users', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
    ]
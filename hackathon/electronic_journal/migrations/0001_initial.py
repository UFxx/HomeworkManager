# Generated by Django 4.2.1 on 2023-12-18 16:14

import autoslug.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='username', unique=True, verbose_name='URL')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон')),
                ('verification', models.BooleanField(default=False, verbose_name='Верификация')),
                ('role', models.CharField(choices=[('admin', 'admin'), ('student', 'student')], default='student', max_length=50, verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название группы')),
                ('curs', models.IntegerField(blank=True, default=1, null=True, verbose_name='Курс')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest_name', models.CharField(max_length=100, verbose_name='Задание')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('file_link', models.FileField(blank=True, null=True, upload_to='quest/%Y/%m/%d/')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Дата Добавлена')),
                ('date_pass', models.DateField(blank=True, verbose_name='Дата сдачи')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic_journal.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50, verbose_name='Название')),
                ('subject_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Код предмета')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='UserQuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, verbose_name='Статус')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('file_link', models.FileField(blank=True, null=True, upload_to='user_quest/%Y/%m/%d/')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='electronic_journal.quest', verbose_name='Задание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.AddField(
            model_name='quest',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic_journal.subject', verbose_name='Предмет'),
        ),
        migrations.AddField(
            model_name='quest',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель'),
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='electronic_journal.group', verbose_name='Группа'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
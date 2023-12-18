from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from sortedm2m.fields import SortedManyToManyField
from autoslug import AutoSlugField


class User(AbstractUser):
    CHOICES = (
        ('admin', 'admin'),
        ('student', 'student'),
    )
    group = models.ForeignKey('Group', on_delete=models.PROTECT, verbose_name='Группа', blank=True, null=True)
    slug = AutoSlugField(populate_from='username', unique=True, db_index=True, verbose_name='URL', )
    phone = models.CharField(max_length=15, verbose_name='Телефон', blank=True, null=True)
    verification = models.BooleanField(default=False, verbose_name='Верификация')
    role = models.CharField(max_length=50, choices=CHOICES, verbose_name='Роль', default='student')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название группы')
    curs = models.IntegerField(default=1, verbose_name='Курс', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject_name = models.CharField(max_length=50, verbose_name="Название")
    subject_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="Код предмета")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return f"{self.subject_name}-{self.subject_code}"


class Quest(models.Model):
    quest_name = models.CharField(max_length=100, verbose_name='Задание')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    teacher = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Преподаватель')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    file_link = models.FileField(upload_to='quest/%Y/%m/%d/', blank=True, null=True)
    date_added = models.DateField(auto_now_add=True, blank=True, verbose_name='Дата Добавления')
    date_pass = models.DateField(blank=True, verbose_name='Дата сдачи')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return f"{self.quest_name}-{self.date_added}"


class UserQuest(models.Model):
    status = models.BooleanField(default=True, verbose_name='Статус')
    quest = models.ForeignKey(Quest, on_delete=models.PROTECT, verbose_name='Задание')
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Студент')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    file_link = models.FileField(upload_to='user_quest/%Y/%m/%d/', blank=True, null=True)
    date_added = models.DateField(auto_now_add=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', blank=True, null=True)

    class Meta:
        verbose_name = 'Готовая работа'
        verbose_name_plural = 'Готовые работы'

    def __str__(self):
        return f"{self.user}-{self.quest}-{self.date_added}"

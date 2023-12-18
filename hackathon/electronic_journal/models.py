from django.db import models

class Group(models.Model):
    description = models.CharField(max_length=255)
    curs = models.BigIntegerField()
    beebebebeb = models.BigIntegerField()

class Subject(models.Model):
    subject_title = models.BigIntegerField()
    description = models.CharField(max_length=255)
    bebebeb = models.BigIntegerField()

class Quest(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey('User', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    file_link = models.CharField(max_length=255)

class UserQuest(models.Model):
    status = models.CharField(max_length=255)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    file_link = models.CharField(max_length=255, null=True)

class User(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    FIO = models.CharField(max_length=255)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    verification = models.BinaryField(max_length=16)
    role = models.CharField(max_length=255)

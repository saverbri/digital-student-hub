from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Студент'),
        ('teacher', 'Преподаватель'),
        ('admin', 'Администратор'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    course_group = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100, blank=True)

    def is_student(self):
        return self.role == 'student'
    def is_teacher(self):
        return self.role == 'teacher'
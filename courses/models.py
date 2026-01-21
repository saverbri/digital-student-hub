from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    students = models.ManyToManyField(User, related_name='enrolled_courses', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Material(models.Model):
    MATERIAL_TYPES = [
        ('lecture', 'Лекция'),
        ('practice', 'Практическая работа'),
        ('video', 'Видео'),
        ('book', 'Учебник'),
        ('other', 'Другое'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=200)
    material_type = models.CharField(max_length=20, choices=MATERIAL_TYPES)
    file = models.FileField(upload_to='materials/', blank=True, null=True)
    content = models.TextField(blank=True)
    external_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.title} ({self.course})"
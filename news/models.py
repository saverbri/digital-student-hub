from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class News(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'Общие новости'),
        ('academic', 'Учебные новости'),
        ('events', 'Мероприятия'),
        ('announcements', 'Объявления'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
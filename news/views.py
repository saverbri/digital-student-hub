from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news = News.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    news.views += 1
    news.save()
    return render(request, 'news/news_detail.html', {'news': news})
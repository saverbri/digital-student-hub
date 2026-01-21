from django.shortcuts import render
from news.models import News

def home(request):
    latest_news = News.objects.filter(is_published=True).order_by('-created_at')[:4]
    return render(request, 'home.html', {'latest_news': latest_news})

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    context = {'user': request.user}
    return render(request, 'dashboard.html', context)
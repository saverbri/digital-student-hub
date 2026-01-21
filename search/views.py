from django.shortcuts import render
from django.db.models import Q
from courses.models import Course, Material
from news.models import News

def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        courses = Course.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            is_published=True
        )
        materials = Material.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        news = News.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            is_published=True
        )
        results = {
            'courses': courses,
            'materials': materials,
            'news': news,
        }
    return render(request, 'search/results.html', {'query': query, 'results': results})
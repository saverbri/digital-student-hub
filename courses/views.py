from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Material

def course_list(request):
    courses = Course.objects.filter(is_published=True)
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def course_materials(request, slug):
    course = get_object_or_404(Course, slug=slug)
    materials = course.materials.all()
    return render(request, 'courses/materials.html', {'course': course, 'materials': materials})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    
    progress = 0
    if request.user.is_authenticated and request.user in course.students.all():
        # Простая логика расчета прогресса
        total_materials = course.materials.count()
        if total_materials > 0:
            # Здесь можно добавить логику просмотренных материалов
            progress = 25  # Пример: 25% пройдено
    
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'progress': progress
    })
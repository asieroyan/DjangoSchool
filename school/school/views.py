from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render


from .models import Class, Student


# Create your views here.
def index(request):
    classes = Class.objects.all()
    context = {
        'classes': classes,
    }
    return render(request, 'school/index.html', context)


def detail(request, class_id):
    class_object = get_object_or_404(Class, pk=class_id)
    return render(request, 'school/detail.html', {'class': class_object})

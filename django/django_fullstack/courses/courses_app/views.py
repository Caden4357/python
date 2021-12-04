from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages


def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def create_course(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            # print(errors)
            return redirect('/')
        course = Course.objects.create(
        name = request.POST['name'],
        desc = request.POST['desc']
    )
        return redirect('/')
    else:
        return redirect('/')

def course_delete(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'delete.html', context)

def delete_course(request, id):
    to_delete = Course.objects.get(id=id)
    to_delete.delete()
    return redirect('/')
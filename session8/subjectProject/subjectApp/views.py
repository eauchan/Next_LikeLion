from django.shortcuts import render, redirect
from .models import Subject, Major
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

# Create your views here.

class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

def home(request):
    subjects = Subject.objects.all()
    majors = Major.objects.all()
    return render(request, 'home.html', {'subjects': subjects, 'majors': majors})

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')

def DeleteSubjectView(request, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')

def computerSubjectView(request):
    subjects = Subject.objects.all()
    computerMajor = subjects.filter(major__name='컴퓨터학과')

    return render(request, 'computer.html', {'computerMajor': computerMajor})
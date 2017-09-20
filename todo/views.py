# coding:utf-8
from django.shortcuts import render,redirect
from .models import TodoEnvet
from .forms import TodoEnvetForm
# Create your views here.

def todo_event(request):
    events = TodoEnvet.objects.all()
    if request.method == 'POST':
        form = TodoEnvetForm(request.POST)
        if form.is_valid():
            form.save()
        form = TodoEnvetForm()
        return render(request, 'index.html', {'form': form, 'events': events})
    else:
        form = TodoEnvetForm()
        return render(request,'index.html',{'form': form, 'events': events})

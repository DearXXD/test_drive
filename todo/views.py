# coding:utf-8
from django.shortcuts import render
from .models import TodoEnvet
from .forms import TodoEnvetForm
# Create your views here.

def todo_event(request):
    '''
    处理待办事项,初始化--回显--保存
    :param request: form
    :return: page and data
    '''
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

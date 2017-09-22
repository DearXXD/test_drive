# coding:utf-8
from django.shortcuts import render,redirect
from .models import TodoEvent
from .forms import TodoEnvetForm
# Create your views here.


def todo_event(request):
    '''
    处理待办事项,初始化--回显--保存
    :param request: form
    :return: page and data
    '''
    events = TodoEvent.objects.all()
    if request.method == 'POST':
        form = TodoEnvetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = TodoEnvetForm()
        return render(request,'index.html',{'form': form, 'events': events})

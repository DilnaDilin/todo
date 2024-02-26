from django.shortcuts import render, redirect
from .models import Task
from .form import todoForm
# Create your views here.
def home(request):
    tasklist=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
        return redirect('/')

    return render(request,'home.html',{'tasklist':tasklist})
def delete(request,id):
    if request.method=='POST':
        task=Task.objects.get(id=id)
        print(task)
        task.delete()
        return redirect('/')

    return render(request,'delete.html')
def edit(request,id):
    task=Task.objects.get(id=id)
    form=todoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')


    return render(request,'edit.html',{'task':task, 'form':form})
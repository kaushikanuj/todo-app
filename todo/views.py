from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import TodoApp


# Create your views here.
def home(request):
    data = TodoApp.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm()
    context = {'form': form, 'data': data}
    return render(request, 'todo/index.html', context)


def user_update(request, pk):
    data = TodoApp.objects.get(id=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm(instance=data)
    return render(request, 'todo/update.html', {'form': form})


def user_delete(request, pk):
    data = TodoApp.objects.get(id=pk)
    data.delete()
    return redirect('/')

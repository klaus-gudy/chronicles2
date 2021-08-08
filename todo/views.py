from django.shortcuts import render
from .forms import TodoForm
from .models import Todo
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import get_object_or_404
from django.contrib  import messages

def index(request):
    todos = Todo.objects.all()

    complete = todos.filter(is_completed=True).count()
    incomplete = todos.filter(is_completed=False).count()
    all_count = todos.count()


    context = {'todos':todos, 'complete':complete , 'incomplete':incomplete , 'all_count':all_count}

    return render(request,  'todo/index.html', context)
  

def create(request):
    form = TodoForm()
    context = {'form': form}

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed', False)

        todo = Todo()

        todo.title = title
        todo.description = description
        todo.is_completed = True if is_completed =="on" else False

        todo.save()

        messages.add_message(request, messages.SUCCESS, "CREATED successful")

        return HttpResponseRedirect(reverse("details", kwargs={'id': todo.pk}))

    return render(request,  'todo/create.html', context)    

def details(request, id):
    todo = get_object_or_404(Todo, pk = id)

    context = {'todo': todo}

    return render(request,  'todo/details.html', context )  

def delete(request, id):
    todo = get_object_or_404(Todo, pk = id)

    context = {'todo': todo}

    if request.method == "POST":
        todo.delete()

        messages.add_message(request, messages.SUCCESS, "deleted successful")

        return HttpResponseRedirect(reverse('index'))

    return render(request,  'todo/delete.html', context )      

def edit(request, id):
    todo = get_object_or_404(Todo, pk = id)
    form= TodoForm(instance=todo)

    context = {'todo': todo , 'form':form}

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed', False)

        todo.title = title
        todo.description = description
        todo.is_completed = True if is_completed =="on" else False

        todo.save()

        messages.add_message(request, messages.SUCCESS, "edit successful")

        return HttpResponseRedirect(reverse("details", kwargs={'id': todo.pk}))

    return render(request, 'todo/edit.html', context)    
from django.shortcuts import render
from .forms import TodoForm
from .models import Todo
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import get_object_or_404

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

        return HttpResponseRedirect(reverse("details", kwargs={'id': todo.pk}))

    return render(request,  'todo/create.html', context)    

def details(request, id):
    todo = get_object_or_404(Todo, pk = id)

    context = {'todo': todo}

    return render(request,  'todo/details.html', context )  
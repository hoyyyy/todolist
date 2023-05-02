from django.shortcuts import render
from .models import ToDoItem

def todo(request):
    todo_items = ToDoItem.objects.all()

    if request.method == 'POST':

        title = request.POST.get("title")
        description = request.POST.get("description")

        tt = ToDoItem(title=title, description=description)
        tt.save() 

    return render(request, 'todolist/todo.html', {'todo_items': todo_items})
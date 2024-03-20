from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todo = Todo.objects.all()  # Renamed queryset variable to 'todos'
    if request.method == 'POST':
        new_todo = Todo(title=request.POST['title'])  # Corrected reference to Todo model
        new_todo.save()
        return redirect('/')
    return render(request, 'index.html',{'todos':todo})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')
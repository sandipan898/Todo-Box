from django.shortcuts import render, redirect, get_object_or_404
from .forms import ListForm
from django.contrib import messages
from .models import List
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.

@login_required
def welcome_view(request):
    template_name = "todo_list/welcome.html"
    no_of_items = List.objects.count()
    no_of_incomplete_items = List.objects.filter(completed=False).count()
    context = {'no_of_items': no_of_items, 'no_of_incomplete_items': no_of_incomplete_items}
    return render(request, template_name, context)

@login_required
def home_view(request):

    template_name = 'todo_list/home.html'
    context = {}
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            context['objects'] = all_items
            messages.success(request, ("It has been added to the list!"))
    
    else:
        all_items = List.objects.all()
        context['objects'] = all_items
    
    return render(request, template_name, context=context)

@login_required
def delete(request, id):
    item = get_object_or_404(List, id=id)
    item.delete()
    messages.success(request, ('Item has been deleted successfully!'))
    return redirect('home')

@login_required
def done(request, id):
    item = get_object_or_404(List, id=id)
    item.completed = True
    item.save()
    return redirect('home')

@login_required
def undone(request, id):
    item = get_object_or_404(List, id=id)
    item.completed = False
    item.save()
    return redirect('home')

@login_required
def update(request, id):
    template_name = 'todo_list/update.html'
    context = {}
    if request.method == "POST":
        item = get_object_or_404(List, id=id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited'))
            return redirect('home')
    
    else:
        item = get_object_or_404(List, id=id)
        context['object'] = item
        return render(request, template_name, context)


def about_view(request):
    template_name = 'todo_list/about_page.html'
    context = {}
    return render(request, template_name, context)

def contact_view(request):
    template_name = 'todo_list/contact_page.html'
    context = {'emails': ['sandipan.das898@gmail.com', 'sisir.das983@gmail.com'], 
                'github': 'https://github.com/sandipan89',
                'linkedin': 'https://www.linkedin.com/in/sandipan-das-528166175/',
                }
    return render(request, template_name, context)

def help_view(request):
    template_name = 'todo_list/help_page.html'
    context = {}
    return render(request, template_name, context)
from django.shortcuts import render, redirect
from .models import Category
from .forms import SearchForm


def main_app(request):
    categories = Category.objects.all()
    return render(request, 'main.html', {'category': categories})


def shop(request):
    categories = Category.objects.all()
    return render(request, 'men.html', {'category': categories})

def register(request):
    if request.method == 'POST':
        form = Category(request.POST)
        if form.is_valid():
            print('yes')
            form.save()
        return redirect('login')
    else:
        form = SearchForm()
    return render(request, 'users/register.html', {'form': form})

def search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Category.objects.filter(name=query)
    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})


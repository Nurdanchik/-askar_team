from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

from .models import ContactMessage
from .forms import ContactMessageForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index') 
    else:
        form = ContactMessageForm()

    return render(request, 'core/contact.html', {'form': form})

def suggestions(request):

    suggestions = ContactMessage.objects.all()

    return render(request, 'core/suggestions.html', {'suggestions': suggestions})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
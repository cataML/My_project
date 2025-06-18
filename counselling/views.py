from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thank you for contacting us.')
            return redirect('counselling')
    else:
        form = ContactForm()
        return render(request, 'counselling/index.html', {'form': form})



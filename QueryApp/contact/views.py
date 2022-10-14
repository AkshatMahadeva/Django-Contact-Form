from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            print("form saved!")
            messages.success(request, "form submitted successfully!")
        else:
            print("form not saved")
            messages.error(request, "please enter valid input")
    contact = ContactForm()
    context = {'form' : contact}
    return render(request, 'contact.html', context=context)
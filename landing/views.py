from django.http.response import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import SubscriberForm

def sey_something(request):
    name = "Program title"
    date = timezone.now()
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())
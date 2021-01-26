from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, render_to_response

from django.template import RequestContext
from django.urls import reverse
from django.views import View
from django.core.mail import EmailMessage

# Create your views here.
from .forms import Contact


class Index(View):
    def get(self, request, *args, **kwargs):
        form = Contact()
        context = {'form': form}
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        form = Contact(request.POST)
        context = {'form': form}
        if form.is_valid():
            message= form.cleaned_data['message']

            email = EmailMessage(
                subject='website message',
                body=message,
                from_email='mustansir.jhaveri@betterinfotech.com',
                to=['mustansir.jhaveri@betterinfotech.com']
            )
            email.send()
            return redirect('accounts:index')
        else:
            return render(request, 'index.html', context)

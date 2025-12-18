from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.views import View


def main(request):
    return HttpResponse("Hello")

class MainClass(View):
    def get(self, request):
        return HttpResponse("Hello")


def home(request):
    return render(request, 'core/home.html')

class HomeClass(View):
    def get(self, request):
        return render(request, 'core/home.html')


def context(request):
    return render(request, 'core/context.html', {'name': 'jeka'})

class ContextClass(View):
    name = 'jeka'
    def get(self, request):
        return render(request, 'core/context.html', {'name': self.name})

class ContextClass2(ContextClass):
    def get(self, request):
        return render(request, 'core/context.html', {'name': self.name})


def news(request, template_name):
    template_name = template_name
    return render(request, template_name, {'info': 'Hello My name is jeka.'})

class NewsClass(View):
    def get(self, request, template_name):
        self.teamplate_name = template_name
        return render(request, template_name, {'info': 'Hello My name is jeka.'})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Form is submitted!!")
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

class ContactClass(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'core/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Form is submitted!!")

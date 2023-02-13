from django.shortcuts import render, redirect
from .models import ContactUs
from .forms import ContactUsForm
# from django.views.generic import CreateView
# from django.urls import reverse_lazy

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            ContactUs.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = ContactUsForm()
    return render(request, 'contact/contact.html', context={'form':form})


# '''
#     Use forms for input info without creating form.py
#         1. [Import] ---> from django.views.generic import CreateView
#         2. [Correct html name] contact-form.html 
#         3. [In urls.py change] ---> path('', views.('name of ur class').as_view(), name='contact'),
#         [as_view()] is special for calling class as object instead if modul(function)
# '''

# class ContactUsFormView(CreateView):
#     ''' instead of create correct html-file with form in the name u can show path manualy '''
#     template_name = 'contact/contact.html'
#     ''' from what model u whant to get info '''
#     model = ContactUs
#     ''' creating fields by the names of atributes (better to write every of them) ---> ['__all__'] NOT working '''
#     fields = ['full_name', 'email', 'company', 'text']
#     ''' 
#         where the enter buttun will get u after the input 
#         ---> from django.urls import reverse_lazy ---> ...
#     '''
#     success_url = reverse_lazy('contact')


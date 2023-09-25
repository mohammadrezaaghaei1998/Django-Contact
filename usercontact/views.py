from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contact




def home(request):
    return render(request,'main/home.html')


def contact(request):
    success_message = None
    form = ContactForm()  

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            contact = Contact(
                name=name,
                email=email,
                message=message
            )
            contact.save()

            success_message = 'Your message has been sent successfully!'
            return redirect('success')

    return render(request, 'main/contact.html', {'form': form, 'success_message': success_message})



def success(request):
    return render(request,'main/success.html')
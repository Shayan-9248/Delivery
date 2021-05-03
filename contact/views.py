from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib import messages


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        message = f'Name: {name} \n Email Address: {email} \n Subject: {subject} \n Message: {body}'
        form = EmailMessage(
            'Contact Us',
            message,
            'test',
            (email,)
        )
        messages.success(request, 'Thank you for your Contact', 'success')
        form.send(fail_silently=False)
    return render(request, 'contact/contact.html')
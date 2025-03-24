from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .contact_form import ContactForm
from django.contrib.auth.decorators import login_required


@login_required
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Creamos el correo
            email = EmailMessage(
                "Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["carlosterrezsegura@gmail.com"],
                reply_to=[email]
            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Everytthing's ok, redirect to OK
                return redirect(reverse('contact') + "?ok")
            except:
                # Something's wrong, redirect to FAIL
                return redirect(reverse('contact') + "?fail")

    return render(request, "contact/contact.html", {'form': contact_form})
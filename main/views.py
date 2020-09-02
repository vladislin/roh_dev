from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News, Product, MainImage
from .forms import ContactUsForm


def home(request):
    return render(request, 'main/home.html', {'news': News.objects.order_by("-date")[:3],
                                              'img': MainImage.objects.all()})


def dilers(request):
    return render(request, 'main/diler.html')


class ShowNewsView(ListView):
    model = News
    template_name = 'main/inner-page.html'
    context_object_name = 'news'
    ordering = ['-date']


class NewsDetailView(DetailView):
    model = News
    template_name = 'main/portfolio-details.html'


def portfolio_view(request):
    return render(request, 'main/portfolio.html', {'product': Product.objects.all()})


def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data
            sender = contact_form.cleaned_data
            phone = contact_form.cleaned_data
            subject = contact_form.cleaned_data['subject']
            message = 'Ви отримали нове повідомлення від {} ({}).\n' \
                      'Номер телефону користувача: {} \n\n'.format(name['name'], sender['sender'], phone['phone'])
            message += contact_form.cleaned_data['message']
            recipients = ['on_ig@i.ua', 'rohatynska.sender@gmail.com']
            send_mail(subject, message, 'rohatynska.sender@gmail.com', recipients)

    else:
        contact_form = ContactUsForm()

    return render(request, 'main/success.html', {
        'form': contact_form,
    })

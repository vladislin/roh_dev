from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    View
)

from .forms import ContactUsForm
from .models import News, Product, MainImage


class HomeView(TemplateView):
    """ Main page view """

    template_name = 'main/pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.order_by("-date")[:3]
        context['img'] = MainImage.objects.filter(status=True)
        return context


class NewsView(ListView):
    """All News page view"""

    model = News
    template_name = 'main/pages/news.html'
    context_object_name = 'news'
    ordering = ['-date']


class NewsDetailView(DetailView):
    """News detail page view"""
    model = News
    template_name = 'main/pages/news-details.html'


class ProductionView(TemplateView):
    """ Portfolio page view """
    template_name = 'main/pages/production.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.all()
        return context


class ForDilersView(View):
    """ For Dilers page view """

    def get(self, request, *args, **kwargs):
        return render(request, 'main/pages/diler.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ContactUsForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                sender = form.cleaned_data['sender']
                phone = form.cleaned_data['phone']
                subject = form.cleaned_data['subject']
                message = f'Ви отримали нове повідомлення від {name} ({sender}).\n' \
                          f'Номер телефону користувача: {phone} \n\n'
                message += form.cleaned_data['message']
                recipients = ['on_ig@i.ua', 'config.sender@gmail.com']
                send_mail(subject, message, 'config.sender@gmail.com', recipients)

                return HttpResponse('Дякуємо. З вами скоро зв\'яжуться!')
            else:
                return HttpResponse('Виникла помилка, спробуйте ще раз!')

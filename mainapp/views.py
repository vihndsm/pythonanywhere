from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio
from django.core.mail import send_mail
import telebot
from .forms import ApplicationsForm
from django.views import View

bot = telebot.TeleBot('1104474861:AAEe7_kXP84eEpiK3gNmqOQPjPnUclgkpeI')

def index(request):
    port = Portfolio.objects.all()
    form = ApplicationsForm()
    return render(request, 'mainapp/index.html', {'portfolio': port, 'form': form})

class ApplicationsView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ApplicationsForm(request.POST)
            if form.is_valid():
                form.save()
                mail = form.cleaned_data['mail']
                name = form.cleaned_data['name']
                comment = form.cleaned_data['comment']
                subject = 'Новая заявка на подписку!'
                from_email = 'vihndsm@gmail.com'
                to_email = ['chynar1965@gmail.com']
                message = 'Новая заявка!' + '\r\n' + '\r\n' + 'Почта: ' + mail + '\r\n' + '\r\n' + 'Имя:' + name + '\r\n' + 'Коммент' + comment
                send_mail(subject, message, from_email, to_email, fail_silently=False)
                bot.send_message(485412013, message)
        return redirect('home')


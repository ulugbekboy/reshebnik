from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
import telebot




token = "1525648534:AAGUxjE_HtNVmUHgTp2eKCEeJZGYNyFHb3A"
bot = telebot.TeleBot(token)


def index(request):

    accordition= Accordition.objects.all()
    b = Bajar.objects.all().first()
    otziv =Otziv.objects.all()
    contact = Contacts.objects.all().first()





    context= {


        'accordition':accordition,
        'b':b,
        'otziv':otziv,
        'contact':contact
    }
    return render(request , 'index.html', context)


def rus(request):
    accordition = Accordition.objects.all()
    b = Bajar.objects.all().first()
    otziv = Otziv.objects.all()
    contact = Contacts.objects.all().first()

    context = {

        'accordition': accordition,
        'b': b,
        'otziv': otziv,
        'contact': contact
    }

    return render(request,'rus.html', context)

def contact(request):


    form = ContactFormForm()

    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        messages.success(request, 'Request were send.')

        
        if form.is_valid():
            form.save()

            message_name= request.POST['name']
            message_phone= request.POST['phone']
            message_avatar = request.POST['avatar']
            message_text= request.POST['message']
            sms = f'📩 Sizga xabar keldi\n\nIsmi: {message_name}\n☎{message_avatar}️ Telefon raqami: {message_phone} \n✉️ Xabar: {message_text}'
            bot.send_message(196862960 , sms)
            return redirect('index')

    
    context={
            'form':form,


        }
    return render(request , 'contact.html' , context)







    




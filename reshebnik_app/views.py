from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
import telebot




token = "1525648534:AAGUxjE_HtNVmUHgTp2eKCEeJZGYNyFHb3A"
bot = telebot.TeleBot(token)


def index(request):
    try:
        message=Contacts.objects.all().first()
    except:
        message='sorry'


    context= {
        'message':message
    }
    return render(request , 'index.html', context)


def contact(request):
    form = ContactFormForm()
    
    if request.method =='POST':
        form = ContactFormForm(request.POST)
        messages.success(request, 'Request were send.')
        
        if form.is_valid():
            form.save()
            
            try:
                message_name= request.POST['name']
                message_phone= request.POST['phone']
                message_text= request.POST['message']
                sms = f'📩 Sizga xabar keldi\n\nIsmi: {message_name}\n☎️ Telefon raqami: {message_phone} \n✉️ Xabar: {message_text}'
                bot.send_message(196862960 , sms)
                return redirect('index')

            except:
                message_name= request.POST['name']
                message_phone= request.POST['phone']
                sms = f'📩 Sizga xabar keldi\n\nIsmi: {message_name}\n☎️ Telefon raqami: {message_phone} '
                bot.send_message(196862960 , sms)
                return redirect('index')
        

    
    context={
            'form':form,


        }
    return render(request , 'indexing.html' , context)







    




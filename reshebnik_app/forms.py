from django import forms

from .models import *

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactFormUs
        fields = ['name', 'phone', 'message', 'avatar']
        widgets = {
            'name': forms.TextInput(attrs={ 'class' :"w-100 mt-20 fname",'type':"text","name":"fname" ,'value':"",   'placeholder':"Ismingiz *", 'required':'' }),


            'phone': forms.TextInput(attrs={'name':"phone" ,'class' :"w-100 mt-20 phone" ,'type':"text" , 'required':'', 'data-value':"+___(__)___-__-__", 'placeholder': 'Telefon raqamingiz *','value':"" }),
            'avatar': forms.TextInput(
                attrs={'class': "w-100 mt-20 lname", 'name': "lname", 'type': "digit", 'data-value':"+___(__)___-__-__" ,'placeholder': "Telegram raqamingiz yoki profil *",
                       'value': "", 'required': ''}),



            'message': forms.Textarea(attrs={'class' :"w-100 mt-20 contact_message", 'value':"", 'name':"contact_message" ,'required':'', 'placeholder': 'Xabaringiz'})
        }

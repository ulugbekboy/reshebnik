from django import forms

from .models import *

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactFormUs
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={ 'data-value':'Имя','name':'name','data-error':"Пожалуйста, укажите своё имя" ,  'type': "text", 'class':'_req', 'autocomplete':"off" ,'required':''}),
    
            'phone': forms.TextInput(attrs={ 'class':"_req _phone" ,'data-error':"Пожалуйста, укажите свой номер телефона"  ,'name':"phone" , 'data-value':"+___(__)___-__-__",'type': "tel", 'autocomplete':"off", 'required':''}),

            'message': forms.Textarea(attrs={ 'required':'', 'placeholder': 'Text'}),
        }

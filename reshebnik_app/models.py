from django.db import models


class Temalar(models.Model):
    title = models.CharField(max_length=1000 , verbose_name='Tema')
    content=models.TextField(blank=True, verbose_name='message')
    image =models.ImageField('Image' , upload_to='images')








class Contacts(models.Model):
    
    email = models.EmailField(blank=True, verbose_name='Email Company')
    bot =models.CharField(max_length=200, blank=True, verbose_name='Bot')
    gruppa = models.CharField(max_length=200, blank=True, verbose_name='Gruppa')


    def __str__(self):
        return self.bot
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class ContactFormUs(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name='name')
    phone = models.CharField(max_length=100, blank=True, verbose_name='phone')
    fan = models.CharField(max_length=100 , verbose_name= 'Fan')
    message = models.TextField(blank=True, verbose_name='message')

    def __str__(self):
        return self.name

class Accordition(models.Model):
    question = models.CharField(max_length=1000, verbose_name='Question')
    answer = models.CharField(max_length=1000 , verbose_name='Answers')


# class Loyihalar(models.Model):
#     bajarilgan = 
#     jarayonda =

#     success_rate=
#     awards= 


class Otziv(models.Model):
    name =models.CharField(max_length=1000 , verbose_name='Name')
    image= models.ImageField('Image' , upload_to='images')
    status= models.CharField(max_length=1000 , verbose_name='Status')
    message = models.TextField( verbose_name='Message')
    rang = models.PositiveIntegerField(default=0)

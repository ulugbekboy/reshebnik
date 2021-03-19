from django.db import models


class Temalar(models.Model):
    title = models.CharField(max_length=1000 , verbose_name='Tema')
    content=models.TextField(blank=True, verbose_name='message')
    
    title_ru = models.CharField(max_length=1000, verbose_name='Тема', null=True)
    content_ru = models.TextField(blank=True, verbose_name='сообщение', null=True)
    image =models.ImageField('Image' , upload_to='images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Temalar'
        verbose_name_plural = 'Temalar'

class Contacts(models.Model):
    
    email = models.EmailField(blank=True, verbose_name='Email')
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
    avatar = models.CharField(max_length=100 , verbose_name= 'Fan')
    message = models.TextField(blank=True, verbose_name='message')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ContactForm'
        verbose_name_plural = 'ContactForm'


class Accordition(models.Model):
    question = models.CharField(max_length=1000, verbose_name='Question')
    answer = models.CharField(max_length=1000 , verbose_name='Answers')
    
    question_ru = models.CharField(max_length=1000, verbose_name='Вопросы', null=True)
    answer_ru = models.CharField(max_length=1000, verbose_name='Ответы' , null=True)

    def __str__(self):
        return self.question


    class Meta:
        verbose_name = 'Answer&Question'
        verbose_name_plural = 'Answer&Question'


class Bajar(models.Model):
    bajarilgan = models.CharField(max_length=1000, verbose_name='Bajarilgan')
    bajarilayotgan =models.CharField(max_length=1000 , verbose_name='Bajarilayotgan')

    def __str__(self):
        return self.bajarilgan

    class Meta:
        verbose_name = 'Bajarilgan'
        verbose_name_plural = 'Bajarilgan'


class Otziv(models.Model):
    name =models.CharField(max_length=1000 , verbose_name='Name')
    image= models.ImageField('Image' , upload_to='images')
    status= models.CharField(max_length=1000 , verbose_name='Status')
    content = models.TextField( verbose_name='Message')
    point = models.CharField(max_length=1000 , verbose_name='Points')

    name_ru = models.CharField(max_length=1000, verbose_name='Имя', null=True)
    content_ru = models.TextField(verbose_name='Контент', null=True)
    status_ru = models.CharField(max_length=1000, verbose_name='Cтатус', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Otziv'
        verbose_name_plural = 'Otziv'
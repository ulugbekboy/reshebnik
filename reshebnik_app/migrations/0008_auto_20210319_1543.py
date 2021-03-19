# Generated by Django 3.1.7 on 2021-03-19 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reshebnik_app', '0007_auto_20210308_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='accordition',
            name='answer_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Ответы'),
        ),
        migrations.AddField(
            model_name='accordition',
            name='question_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Вопросы'),
        ),
        migrations.AddField(
            model_name='otziv',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='otziv',
            name='name_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='otziv',
            name='point_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Поинты'),
        ),
        migrations.AddField(
            model_name='temalar',
            name='content_ru',
            field=models.TextField(blank=True, null=True, verbose_name='сообщение'),
        ),
        migrations.AddField(
            model_name='temalar',
            name='title_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Тема'),
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reshebnik_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accordition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000, verbose_name='Question')),
                ('answer', models.CharField(max_length=1000, verbose_name='Answers')),
            ],
        ),
        migrations.CreateModel(
            name='Otziv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Name')),
                ('image', models.ImageField(upload_to='images', verbose_name='Image')),
                ('status', models.CharField(max_length=1000, verbose_name='Status')),
                ('message', models.TextField(verbose_name='Message')),
                ('rang', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='address',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='phone',
        ),
        migrations.AddField(
            model_name='contactformus',
            name='fan',
            field=models.CharField(default=False, max_length=100, verbose_name='Fan'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='bot',
            field=models.CharField(blank=True, max_length=200, verbose_name='Bot'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='gruppa',
            field=models.CharField(blank=True, max_length=200, verbose_name='Gruppa'),
        ),
    ]

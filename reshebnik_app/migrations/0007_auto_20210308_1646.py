# Generated by Django 3.1.7 on 2021-03-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reshebnik_app', '0006_auto_20210308_1638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accordition',
            options={'verbose_name': 'Answer&Question', 'verbose_name_plural': 'Answer&Question'},
        ),
        migrations.AlterModelOptions(
            name='bajar',
            options={'verbose_name': 'Bajarilgan', 'verbose_name_plural': 'Bajarilgan'},
        ),
        migrations.AlterModelOptions(
            name='contactformus',
            options={'verbose_name': 'ContactForm', 'verbose_name_plural': 'ContactForm'},
        ),
        migrations.AlterModelOptions(
            name='otziv',
            options={'verbose_name': 'Otziv', 'verbose_name_plural': 'Otziv'},
        ),
        migrations.AlterModelOptions(
            name='temalar',
            options={'verbose_name': 'Temalar', 'verbose_name_plural': 'Temalar'},
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='otziv',
            name='point',
            field=models.CharField(max_length=1000, verbose_name='Points'),
        ),
    ]

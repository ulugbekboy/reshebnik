# Generated by Django 3.1.7 on 2021-03-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reshebnik_app', '0004_auto_20210306_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bajar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bajarilgan', models.CharField(max_length=1000, verbose_name='Bajarilgan')),
                ('bajarilayotgan', models.CharField(max_length=1000, verbose_name='Bajarilayotgan')),
            ],
        ),
    ]

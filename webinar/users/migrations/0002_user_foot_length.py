# Generated by Django 2.2.19 on 2023-05-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='foot_length',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Размер ноги'),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-30 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marcair', '0008_airport_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_email_adress',
            field=models.EmailField(default='anonymous@marcairlines.com', help_text='ex : pierre.niney@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
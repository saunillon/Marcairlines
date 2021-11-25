# Generated by Django 3.2.9 on 2021-11-23 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marcair', '0004_auto_20211123_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airport',
            old_name='name',
            new_name='airport_name',
        ),
        migrations.AddField(
            model_name='client',
            name='client_adress',
            field=models.CharField(default='rue du Général de Gaulle, Vichy', help_text='ex : 16 rue de la paix, 75000 Paris', max_length=100),
            preserve_default=False,
        ),
    ]
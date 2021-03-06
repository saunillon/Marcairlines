# Generated by Django 3.2.9 on 2021-11-22 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Marcair', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='arrival_airport_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='arrival', to='Marcair.airport'),
        ),
        migrations.AlterField(
            model_name='connection',
            name='departure_airport_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departure', to='Marcair.airport'),
        ),
    ]

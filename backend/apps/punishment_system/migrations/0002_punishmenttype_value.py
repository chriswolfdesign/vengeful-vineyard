# Generated by Django 3.0.3 on 2020-02-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punishment_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='punishmenttype',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]

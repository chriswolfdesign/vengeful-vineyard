# Generated by Django 3.0.3 on 2020-03-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punishment_system', '0005_auto_20200301_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='punishment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
# Generated by Django 3.0.3 on 2020-02-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20200205_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='date',
            field=models.CharField(default='', max_length=100),
        ),
    ]

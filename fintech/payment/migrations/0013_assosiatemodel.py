# Generated by Django 3.0.3 on 2020-02-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0012_register_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssosiateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orguser', models.CharField(max_length=7)),
                ('account_no', models.CharField(max_length=10)),
                ('ass_user', models.CharField(max_length=7)),
            ],
        ),
    ]

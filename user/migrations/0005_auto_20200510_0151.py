# Generated by Django 3.0.6 on 2020-05-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200510_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zipcode',
            name='code',
            field=models.CharField(max_length=7),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-10 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200510_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='zipcode',
        ),
        migrations.AlterField(
            model_name='linkcommande',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='ZipCode',
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20200514_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='postale_code',
            field=models.CharField(max_length=6, null=True, verbose_name='Code postale'),
        ),
    ]
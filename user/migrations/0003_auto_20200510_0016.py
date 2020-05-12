# Generated by Django 3.0.6 on 2020-05-10 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200509_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='profil',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='adress',
            name='zipcode',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='user.ZipCode'),
            preserve_default=False,
        ),
    ]

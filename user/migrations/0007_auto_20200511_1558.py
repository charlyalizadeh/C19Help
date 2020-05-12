# Generated by Django 3.0.6 on 2020-05-11 15:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200510_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkcommande',
            name='commande',
        ),
        migrations.AddField(
            model_name='linkcommande',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='linkcommande',
            name='profil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Profil'),
        ),
        migrations.AlterField(
            model_name='linkcommande',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Product'),
        ),
        migrations.DeleteModel(
            name='Commande',
        ),
    ]
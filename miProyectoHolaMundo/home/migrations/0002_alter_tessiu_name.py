# Generated by Django 3.2.9 on 2021-11-24 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tessiu',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.paciente', verbose_name='nombre'),
        ),
    ]
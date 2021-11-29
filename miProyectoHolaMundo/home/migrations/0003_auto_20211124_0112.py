# Generated by Django 3.2.9 on 2021-11-24 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_tessiu_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tessiu',
            name='inflamation',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tessiu',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.paciente', verbose_name='nombre'),
        ),
    ]
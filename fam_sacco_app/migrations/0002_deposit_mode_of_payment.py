# Generated by Django 4.2.6 on 2023-10-19 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fam_sacco_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='mode_of_payment',
            field=models.CharField(choices=[('banked', 'banked'), ('mobile money', 'mobile money'), ('cash', 'cash')], default='cash', max_length=30),
        ),
    ]

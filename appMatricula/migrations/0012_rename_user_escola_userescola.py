# Generated by Django 5.0.3 on 2024-04-15 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMatricula', '0011_escola_endereco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='escola',
            old_name='user',
            new_name='userEscola',
        ),
    ]
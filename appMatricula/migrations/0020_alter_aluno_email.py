# Generated by Django 5.0.3 on 2024-04-20 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMatricula', '0019_aluno_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
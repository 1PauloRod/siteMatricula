# Generated by Django 5.0.3 on 2024-05-08 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMatricula', '0033_alter_aluno_aniversario'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=7, null=True, unique=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-20 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMatricula', '0024_alter_aluno_cpf_alter_aluno_rg_alter_aluno_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='rg',
            field=models.CharField(max_length=12),
        ),
    ]
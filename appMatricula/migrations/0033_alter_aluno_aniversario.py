# Generated by Django 5.0.3 on 2024-04-27 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMatricula', '0032_alter_aluno_aniversario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='aniversario',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
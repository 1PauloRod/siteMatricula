# Generated by Django 5.0.3 on 2024-05-18 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMatricula', '0035_escola_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='escola',
            name='dataFundacao',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
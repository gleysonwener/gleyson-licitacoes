# Generated by Django 4.1.1 on 2022-09-12 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0005_remove_contatos_assunto_remove_contatos_mensagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatos',
            name='telefone',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Telefone'),
        ),
    ]

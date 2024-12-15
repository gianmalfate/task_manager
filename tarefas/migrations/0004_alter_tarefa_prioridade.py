# Generated by Django 5.1.4 on 2024-12-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tarefas", "0003_remove_tarefa_criacao_tarefa_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarefa",
            name="prioridade",
            field=models.CharField(
                choices=[("alta", "Alta"), ("média", "Média"), ("baixa", "Baixa")],
                default="importante",
                max_length=25,
            ),
        ),
    ]

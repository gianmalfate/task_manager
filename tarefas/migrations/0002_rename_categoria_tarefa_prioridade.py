# Generated by Django 5.1.4 on 2024-12-13 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tarefas", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tarefa",
            old_name="categoria",
            new_name="prioridade",
        ),
    ]

# Generated by Django 4.2.11 on 2024-03-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nappy_changes", "0003_alter_nappychange_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nappychange",
            name="notes",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

# Generated by Django 4.2.11 on 2024-04-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nappy_changes", "0005_alter_nappychange_nappy_contents"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nappychange",
            name="notes",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

# Generated by Django 4.2.11 on 2024-03-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feeds", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feed",
            name="breast_feed_time_minutes",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="feed",
            name="formula_amount_ml",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

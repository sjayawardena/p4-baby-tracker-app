# Generated by Django 4.2.11 on 2024-03-23 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nappy_changes', '0002_alter_nappychange_notes_alter_nappychange_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nappychange',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nappy_changes_list', to=settings.AUTH_USER_MODEL),
        ),
    ]

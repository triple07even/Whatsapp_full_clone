# Generated by Django 3.1.6 on 2021-02-25 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_phonebook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactlist',
            name='phone_owner',
        ),
        migrations.AddField(
            model_name='phonebook',
            name='phone_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_stored_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 3.0.2 on 2020-01-27 18:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import website.utils.db_fields.file_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', website.utils.db_fields.file_fields.ResizedHashNameImageField(upload_to='photos', verbose_name='Foto')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Uploaddatum')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Gebruiker')),
            ],
        ),
    ]
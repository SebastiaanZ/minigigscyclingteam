# Generated by Django 3.0.2 on 2020-01-27 13:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import website.utils.db_fields.file_fields


class Migration(migrations.Migration):

    replaces = [('userprofile', '0001_add_basic_user_profile'), ('userprofile', '0002_update_user_profile'), ('userprofile', '0003_use_resized_image_field_for_avatar')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_cyclist', models.BooleanField(default=False, verbose_name='Is this a member of team?')),
                ('profile_picture', website.utils.db_fields.file_fields.ResizedHashNameImageField(blank=True, null=True, upload_to='', verbose_name='Profielfoto')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-25 16:53

from django.db import migrations, models
import website.userprofile.models.profile


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_add_basic_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to="", verbose_name='Profielfoto'),
        ),
    ]

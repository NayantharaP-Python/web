# Generated by Django 3.2.13 on 2022-08-10 18:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='Gallery'),
            preserve_default=False,
        ),
    ]

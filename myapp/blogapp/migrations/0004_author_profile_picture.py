# Generated by Django 2.0.4 on 2018-05-13 22:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile_picture',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]

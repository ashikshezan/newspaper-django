# Generated by Django 2.2.7 on 2019-11-07 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0002_post_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_photo',
            field=models.ImageField(default='post_default.jpg', upload_to='post_images', verbose_name='Post Cover'),
        ),
    ]

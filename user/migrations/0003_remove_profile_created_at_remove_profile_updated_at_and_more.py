# Generated by Django 5.0.4 on 2024-06-10 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_image',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=''),
        ),
    ]
# Generated by Django 5.1.4 on 2025-01-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0002_rename_feedback_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='img',
            field=models.ImageField(default='items/client1.jpg', upload_to='items/'),
        ),
        migrations.AlterField(
            model_name='items',
            name='img',
            field=models.ImageField(default='items/client1.jpg', upload_to='items/'),
        ),
    ]

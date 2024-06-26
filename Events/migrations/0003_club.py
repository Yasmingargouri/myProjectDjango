# Generated by Django 5.0.2 on 2024-05-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_rename_events_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fullName', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='images/defaultClub.jpg', upload_to='profile_pics')),
            ],
        ),
    ]

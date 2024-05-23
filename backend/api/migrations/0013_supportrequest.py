# Generated by Django 5.0.6 on 2024-05-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_broker_fb_link_alter_group_fb_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(max_length=254)),
                ('topic', models.CharField(max_length=255)),
                ('details', models.TextField()),
            ],
        ),
    ]

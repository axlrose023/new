# Generated by Django 5.0.1 on 2024-03-07 16:19

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_remove_keyword_broker_broker_is_active_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=70)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name="pva",
            name="cookies",
            field=models.CharField(default="[]", max_length=3000),
        ),
    ]

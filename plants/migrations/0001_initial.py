# Generated by Django 4.2.6 on 2023-10-20 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Plant",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("plant_img", models.ImageField(upload_to="plants/images")),
                ("plant_name", models.CharField(max_length=255)),
                ("condition", models.CharField(max_length=255)),
                ("disease", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

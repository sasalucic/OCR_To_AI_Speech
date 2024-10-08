# Generated by Django 4.2.8 on 2023-12-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UploadedPhoto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="images")),
                ("recognized_text", models.TextField()),
                ("upload_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

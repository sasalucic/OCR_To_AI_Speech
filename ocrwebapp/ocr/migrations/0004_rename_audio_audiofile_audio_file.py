# Generated by Django 4.2.8 on 2023-12-15 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ocr", "0003_remove_audiofile_uploaded_photo_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="audiofile", old_name="audio", new_name="audio_file",
        ),
    ]

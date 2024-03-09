# ocr/models.py
from django.db import models

class UploadedPhoto(models.Model):
    image = models.ImageField(upload_to="images")
    recognized_text = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image.name} - {self.upload_date}"
    
class AudioFile(models.Model):
    audio_file = models.FileField(upload_to="audio")
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.audio_file.name}"
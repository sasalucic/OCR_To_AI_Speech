from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import pytesseract
from PIL import Image
import requests
import os
import cv2
from .forms import PhotoUploadForm
import numpy as np
from django.shortcuts import render, HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .models import UploadedPhoto, AudioFile


def upload_photo(request):
    recognized_text = None
    recognized_photo = None
    sound_generation_history = None
    audio_url = None

    if request.method == 'POST' and request.FILES['photo']:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)

        full_path = os.path.join(settings.MEDIA_ROOT, filename)
        recognized_text = perform_ocr(full_path)

        # Save the UploadedPhoto instance
        recognized_photo = UploadedPhoto.objects.create(image=photo, recognized_text=recognized_text)
        
        # Generate and save the sound directly
        audio_file = generate_sound(request, recognized_text, recognized_photo)
        audio_url = audio_file.audio_file.url
        
        # Retrieve sound generation history
        sound_generation_history = AudioFile.objects.all()

        # Generate and play the sound directly
        audio_url = generate_sound(request, recognized_text, recognized_photo)
        return render(request, 'ocr/upload_photo.html', {
            'recognized_text': recognized_text,
            'recognized_photo': recognized_photo,
            'sound_generation_history': sound_generation_history,
            'audio_url': audio_url,
        })

    return render(request, 'ocr/upload_photo.html', {
        'recognized_text': recognized_text,
        'recognized_photo': recognized_photo,
        'sound_generation_history': sound_generation_history,
    })

def generate_sound(request, text, recognized_photo):
    # Eleven Labs API endpoint
    url = "https://api.elevenlabs.io/v1/text-to-speech/2EiwWnXFnvU5JabPnv8n"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "ad5b3e63da7d1b82698d5fbe818937a0",  # Replace with your actual API key
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5,
        }
    }

    # Make a request to Eleven Labs API to generate sound
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        # Construct the correct path for the audio file
        audio_file_path = os.path.join(settings.MEDIA_ROOT, 'audio', f'{os.path.basename(recognized_photo.image.name)}.mp3')
        audio_content = ContentFile(response.content)

        # Use default_storage to save the audio file
        default_storage.save(audio_file_path, audio_content)

        # Save to AudioFile model
        audio_file = AudioFile.objects.create(audio_file=audio_file_path)

        return audio_file
    else:
        # Handle the error (you can raise an exception, log the error, etc.)
        raise Exception(f"Error: {response.status_code}, {response.text}")
    
def preprocess_image(img):
    # Resize image
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Denoise and sharpen
    denoised_img = cv2.fastNlMeansDenoising(gray_img, None, h=5)
    sharpened_img = cv2.addWeighted(denoised_img, 1.5, gray_img, -0.5, 0)

    # Apply adaptive thresholding
    _, threshold_img = cv2.threshold(sharpened_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return threshold_img

def perform_ocr(image_path):
    # Open the image using OpenCV
    img = cv2.imread(image_path)

    # Preprocess the image
    preprocessed_img = preprocess_image(img)

    # Perform OCR with language specification
    recognized_text = pytesseract.image_to_string(preprocessed_img, config='--psm 6 --oem 3')

    return recognized_text

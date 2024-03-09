# OCR to Speech Django Web Application

This Django web application utilizes OCR (Optical Character Recognition) to convert text from images to speech. The project was conceptualized by a student who aimed to transform scripts into an eBook-like format.

## Overview

The application allows users to upload images containing text. Once uploaded, the text is extracted using OCR technology provided by Pytesseract. Subsequently, the extracted text is passed to the Eleven Labs AI Speech API to convert it into speech.

## Features

- Upload images containing text.
- Extract text from images using OCR (Pytesseract).
- Convert extracted text to speech using the Eleven Labs AI Speech API.
- Seamless integration with Django framework.

## Installation and Setup

To run this project locally, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/sasalucic/OCR_To_AI_Speech.git
   ```

2. Navigate to the project directory:

   ```
   cd C:\...\OCR_To_Speech_Django_Web_App\ocrwebapp
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the Django development server:

   ```
   python manage.py runserver
   ```

5. Access the application in your web browser at `http://127.0.0.1:8000/ocr/upload`.

## Technologies Used

- Django: Web framework for building the application.
- Pytesseract: Python wrapper for Google's Tesseract-OCR Engine.
- Pillow (PIL): Python Imaging Library for image processing.
- OpenCV (cv2): Library for computer vision tasks.
- Eleven Labs AI Speech API: API for converting text to speech.
- Requests: Library for making HTTP requests.
- Numpy: Library for numerical computing.

## Usage

1. Access the web application through your browser.
2. Upload an image containing text using the provided interface.
3. Once uploaded, the text will be extracted using OCR.
4. The extracted text will be converted into speech using the Eleven Labs AI Speech API.
5. Enjoy listening to the converted speech!



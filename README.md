# Image Text Translator

This is a Python-based GUI application that extracts text from an image, translates it into a selected language, and converts the translated text into speech.

## Features
- Extracts text from images using OCR (Tesseract OCR)
- Translates extracted text into Tamil, Hindi, Kannada, Telugu, Japanese, or Malayalam
- Converts translated text into speech using Google Text-to-Speech (gTTS)
- Supports image input via URL
- Simple and interactive GUI using Tkinter

## Requirements
Ensure you have the following installed before running the script:

### Install Dependencies
```sh
pip install pillow pytesseract gtts googletrans==4.0.0-rc1 langcodes tkinter
```

### Install Tesseract OCR
Tesseract OCR is required for text extraction. Download and install it from:
[Tesseract OCR Download](https://github.com/UB-Mannheim/tesseract/wiki)

After installation, update the script to specify the correct path to `tesseract.exe`. Example:
```python
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract
```

## How to Run
1. Clone or download this script.
2. Install dependencies as mentioned above.
3. Run the script using:
   ```sh
   python script.py
   ```
4. Enter an image URL and select a language for translation.
5. Click `Load Image` to process the image.
6. Click `Translate` to extract and translate text.
7. Click `Play Speech` to hear the translated text.

## Notes
- The program uses Google Translate, so an internet connection is required.
- Make sure the image URL is accessible and properly formatted.
- The translated speech is saved as `translated_speech.mp3` and can be played from the script.

## Troubleshooting
- If Tesseract OCR is not recognized, ensure it is installed and the correct path is set in the script.
- If translation doesn't work, ensure you have an active internet connection.
- If an image fails to load, verify the image URL.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it under the terms of the license.

Enjoy using the Image Text Translator!



![image](https://github.com/user-attachments/assets/eb88756c-d858-4978-9120-7fc2166dc5fe)

![image](https://github.com/user-attachments/assets/79e32f3e-6fd1-4d9a-a5f1-430bce151c8a)

## Text Translated

![image](https://github.com/user-attachments/assets/0e329290-a7c9-42c7-b4f1-110b71845d64)


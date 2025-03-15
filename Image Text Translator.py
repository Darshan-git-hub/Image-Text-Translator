from tkinter import *
from tkinter import filedialog
from PIL import Image
from pytesseract import pytesseract
from gtts import gTTS
from googletrans import Translator
from langcodes import *
import urllib.request
import os
import tempfile


class ImageTranslatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Text Translator")

        # create the label and button for selecting the image file
        self.file_label = Label(master, text="Enter image URL:")
        self.file_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.url_entry = Entry(master, width=50,)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)
        self.clear_button = Button(master, text="Clear URL", command=self.clear_text)
        self.clear_button.grid(row=0, column=3, padx=10, pady=10)

        self.clear_text_button = Button(master, text="clear the text box", command=self.clear_commentbox)
        self.clear_text_button.grid(row=2, column=2, padx=10, pady=10)

        self.browse_button = Button(master, text="Load Image", command=self.load_image)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        # create the label and button for translating the image text
        self.lang_label = Label(master, text="Select language for translation:")
        self.lang_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.languages = {"Tamil": "ta", "Hindi": "hi", "Kannada": "kn", "Telugu": "te", "Japanese": "ja","Malayalam":"ml"}
        self.language_var = StringVar(master)
        self.language_var.set("Tamil")  # default language is Tamil
        self.lang_menu = OptionMenu(master, self.language_var, *self.languages.keys())
        self.lang_menu.grid(row=1, column=1, padx=10, pady=10)

        self.translate_button = Button(master, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=1, column=2, padx=10, pady=10)

        self.quit=Button(master,text="Quit",command= root.destroy)
        self.quit.grid(row=2, column=3, padx=10, pady=10)

        # create the label and button for playing the translated text as speech
        self.speech_label = Label(master, text="Click to hear the translated text:")
        self.speech_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.play_button = Button(master, text="Play Speech", command=self.playspeech)
        self.play_button.grid(row=2, column=1, padx=10, pady=10)

        # create the text box for displaying the image text and the translated text
        self.textbox = Text(master, width=80, height=15, wrap=WORD, font=("Arial", 12))
        self.textbox.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    def clear_text(self):
        self.url_entry.delete(0, END)

    def clear_commentbox(self):
        self.textbox.delete('1.0',END)

    def load_image(self):
        url = self.url_entry.get()
        self.image_path = self.download_image(url)

    def download_image(self, url):
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        temp_file.close()
        urllib.request.urlretrieve(url, temp_file.name)
        return temp_file.name

    def translate_text(self):
        try:
            path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = path_to_tesseract
            img = Image.open(self.image_path)
            text = pytesseract.image_to_string(img)
            self.textbox.insert(END, f"Image Text:\n{text}\n\n")
            translator = Translator(service_urls=['translate.google.com'])
            translated_text = translator.translate(text, dest=self.languages[self.language_var.get()]).text
            self.textbox.insert(END, f"Translated Text ({self.language_var.get()}):\n{translated_text}\n\n")
            self.translated_text = translated_text
            language = self.languages[self.language_var.get()]
            speech = gTTS(text=self.translated_text, lang=language, slow=False)
            speech.save("translated_speech.mp3")
            self.textbox.insert(END, f"Speech file saved as translated_speech.mp3 \n\n")
        except:
            self.textbox.insert(END, f"Error: Please select an image file first.\n\n")

    def playspeech(self):
            os.system("start translated_speech.mp3")

root = Tk()
my_gui = ImageTranslatorGUI(root)
root.mainloop()
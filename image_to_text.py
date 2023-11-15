import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Set the path to the Tesseract executable (update this with the correct path)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Define a function to open a file dialog and select an image
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff")])
    return file_path

# Define a function to perform OCR and display the result
def extract_text():
    file_path = select_image()

    if file_path:
        try:
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image, lang='eng')
            result_text.configure(state='normal')
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, text)
            result_text.configure(state='disabled')
        except Exception as e:
            print(f"An error occurred: {e}")

# Create the GUI window and set its title
root = tk.Tk()
root.title("Image to Text Converter")

# Create a label to prompt the user to select an image
label = tk.Label(root, text="Select an image to extract text:")
label.pack()

# Create a button to trigger the image selection and OCR process
extract_button = tk.Button(root, text="Extract Text", command=extract_text)
extract_button.pack()

# Create a text widget to display the extracted text
result_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
result_text.pack()

# Start the GUI main loop
root.mainloop()


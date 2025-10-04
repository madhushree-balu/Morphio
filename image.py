from PIL import Image
import pytesseract



# Set Tesseract path manually on Windows
pytesseract.pytesseract.tesseract_cmd = r'D:\downloads\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Example usage
image_path = 'example.png'  # Your image file path
text = extract_text_from_image(image_path)
print("Extracted Text:\n", text)

from PIL import Image
import os
from hashlib import sha256
from datetime import datetime

# Create the output directory if it doesn't exist
os.makedirs("static/image/output", exist_ok=True)


def hash_file(file_path):
    now = str(datetime.now())
    return sha256((now + file_path).encode('utf-8')).hexdigest()

def convert_image_format(input_path, output_format):
    """
    Convert image format (e.g., PNG to JPG)
    """
    output_path = "static/image/output/" + hash_file(input_path) + "." + output_format
    with Image.open(input_path) as img:
        img.save(output_path, format=output_format.upper())
    return output_path

def resize_image(input_path, new_size):
    """
    Resize image to (width, height)
    """
    input_format = input_path.split('.')[-1]
    output_path = "static/image/output/" + hash_file(input_path) + "." + input_format
    with Image.open(input_path) as img:
        resized = img.resize(new_size)
        resized.save(output_path)
    return output_path

def rotate_image(input_path, angle):
    """
    Rotate image by angle (degrees)
    """
    input_format = input_path.split('.')[-1]
    output_path = "static/image/output/" + hash_file(input_path) + "." + input_format
    with Image.open(input_path) as img:
        rotated = img.rotate(angle, expand=True)
        rotated.save(output_path)
    return output_path

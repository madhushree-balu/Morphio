from PIL import Image
import pytesseract


def extract_text_from_image(image_path):
    image = Image.open(image_path)

    text = pytesseract.image_to_string(image)

    return text

# Example usage
image_path = 'image.png'  
text = extract_text_from_image(image_path)
print("Extracted Text:\n", text)

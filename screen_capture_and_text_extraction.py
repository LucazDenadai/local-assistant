from PIL import ImageGrab
import pytesseract


# Capturar parte da tela
def capture_screen(region=None):
    img = ImageGrab.grab(bbox=region)  # Região pode ser (left, top, right, bottom)
    return img


# Transformar imagem em texto
def extract_text(img):
    return pytesseract.image_to_string(img)


# Exemplo de uso
screen_img = capture_screen(region=(0, 0, 800, 600))
recognized_text = extract_text(screen_img)
print(recognized_text)
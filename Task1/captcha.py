import random
import string
from PIL import Image, ImageDraw, ImageFont

def generate_captcha_text(length=5):
    characters = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choices(characters, k=length))
    return captcha_text

def generate_captcha_image(captcha_text):
    # Create an image with white background
    width, height = 200, 60
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Load a font
    font = ImageFont.truetype("arial.ttf", 36)

    # Draw the text on the image
    bbox = draw.textbbox((0, 0), captcha_text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2
    draw.text((text_x, text_y), captcha_text, font=font, fill='black')

    # Add some noise
    for _ in range(30):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill='black')

    # Add some lines
    for _ in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill='black', width=1)

    return image

# Generate Captcha text
captcha_text = generate_captcha_text()
print("Generated Captcha Text:", captcha_text)

# Generate Captcha image
captcha_image = generate_captcha_image(captcha_text)

# Save the image
captcha_image.save('captcha.png')

# Optionally, show the image
captcha_image.show()

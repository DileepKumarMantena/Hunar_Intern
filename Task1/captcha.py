import random

def generate_captcha_text(length=5):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

# Generate Captcha text
captcha_text = generate_captcha_text()
print("Generated Captcha Text:", captcha_text)

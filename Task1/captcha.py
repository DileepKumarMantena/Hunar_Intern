import random  # Import the random module for generating random characters

def generate_captcha_text(length=5):
    """
    Function to generate a random CAPTCHA text of a given length.
    
    Args:
        length (int): Length of the CAPTCHA text to be generated. Default is 5.
    
    Returns:
        str: A string containing the random CAPTCHA text.
    """
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'  # Define possible characters
    return ''.join(random.choices(characters, k=length))  # Use random.choices to pick 'length' characters and join them

# Generate Captcha text
captcha_text = generate_captcha_text()  # Call the function to generate CAPTCHA text
print("Generated Captcha Text:", captcha_text)  # Print the generated CAPTCHA text

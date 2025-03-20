import re

def generate_fakeimg_url(width, height, alt_text):
    """
    Generate a Fakeimg.pl URL with grey background and descriptive text
    
    Args:
        width (int): Image width
        height (int): Image height
        alt_text (str): Alternative text to use as image text
    
    Returns:
        str: Fakeimg.pl URL
    """
    # URL encode the alt text, replace spaces with +
    text = alt_text.replace(' ', '+')
    
    # Generate Fakeimg.pl URL with grey background
    return f"http://fakeimg.pl/{width}x{height}/?bg=808080&text={text}&font=arial"

def replace_placeholders_in_file(filename):
    """
    Replace placeholder images in an HTML file with Fakeimg.pl URLs
    
    Args:
        filename (str): Path to the HTML file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Regex to find placeholder images
    placeholder_pattern = re.compile(r'<img\s+src="https://via\.placeholder\.com/(\d+)x(\d+)"([^>]*)>')
    
    def replace_image(match):
        width = match.group(1)
        height = match.group(2)
        other_attrs = match.group(3)
        
        # Extract alt text if present
        alt_match = re.search(r'alt="([^"]*)"', other_attrs)
        alt_text = alt_match.group(1) if alt_match else 'Placeholder'
        
        # Generate new Fakeimg.pl URL
        new_url = generate_fakeimg_url(int(width), int(height), alt_text)
        
        return f'<img src="{new_url}"{other_attrs}>'
    
    # Replace all placeholder images
    updated_content = placeholder_pattern.sub(replace_image, content)
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"Processed {filename}")

# List of HTML files to process
html_files = [
    'index.html',
    'service.html', 
    'about-us.html', 
    'contact.html'
]

# Process each file
for file in html_files:
    replace_placeholders_in_file(file)

print("All placeholder images have been replaced.")
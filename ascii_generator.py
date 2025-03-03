from PIL import Image
import tkinter as tk
from tkinter import filedialog
from rich.console import Console
from rich.rule import Rule

console = Console()

# Getting file path from user
def get_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff")])
    
    # Check if the file is a valid image by trying to open it with PIL
    try:
        with Image.open(file_path) as img:
            img.verify()  # Verify if the image is valid
        return file_path  # Return the file path if valid image
    except (IOError, SyntaxError):
        console.print(f"[bold red]The selected file is not a valid image.[/bold red]")
        return None  # Return None if not a valid image

# Generating ASCII art
def image_to_ascii(image_path, row_hieght, model, aspect):
    img = Image.open(image_path).convert('L') # Grayscale
    original_width, original_height = img.size

    # Account for character aspect ratio
    char_aspect_ratio = aspect if isinstance(aspect, (int, float)) and aspect > 0 and aspect <= 1 else 0.5 # Default to 0.5

    # Calculate new width based on row height and aspect ratios
    new_height = row_hieght if isinstance(row_hieght, (int, float)) and row_hieght > 0 else 20 # Default to 20
    new_width = int(original_width / original_height * new_height / char_aspect_ratio)

    img = img.resize((new_width, new_height))

    ascii_models = {
        "blocky": "░▒▓█#@%XO0",
        "shaded": "□◀▼▲■░▒▓█",
        "braille": "⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉",
        "symbols": "•○◘♂♀♪♠♣♦♥",
        "geometric": "◯○◌▶◀▼▲●",
        "rounded": "○◯◌◍◎◉●●",
        "detailed": " .:-=+*#%@",
        "simple": "-+/\\|_ox#*",
        "techy": "0000111111",
        "punctuation": '!\\"#$%&)(*',
        "nature": "~~^^**++==",
        "alphanumeric": "abcdefghij",
        "emoticons": ":-) ;-) :-("
    }

    ascii_chars = ascii_models.get(model, ascii_models["detailed"][0]) # Default to detailed
    char_count = ascii_models.get(model, (ascii_models["detailed"][1]))[1] # Default to detailed

    # Getting key value for chosen model
    value_to_find = ascii_chars
    key = next((k for k, v in ascii_models.items() if v == value_to_find), None)

    console.print(f'[bold green]Complete! Art generated using "{key}" style with {new_height} rows and an aspect ratio of {char_aspect_ratio}[/bold green]')

    ascii_str = ""
    for y in range(new_height):
        for x in range(new_width):
            pixel = img.getpixel((x, y))
            char = ascii_chars[pixel // 25]
            ascii_str += char
        ascii_str += "\n"

    return ascii_str


console.print(Rule('Welcome to the ASCII Art Generator'))

# Getting image to convert
console.print(f'[bold cyan]Please select the image to convert.[/bold cyan]')
image = get_file_path()

# Getting ASCII art height
console.print(f'[bold cyan]How many rows would you like the ASCII art to encompass? (default value is 20)[/bold cyan]')
num_rows = int(input('Enter number of rows: '))

# Getting ASCII art style
console.print(f'[bold cyan]What style would you like to create the ASCII art in? Please tye your selection (default value is "detailed")[/bold cyan]')
console.print(f'[yellow]"detailed", "simple", "blocky", or "lined"[/yellow]')
model = input('Enter selection: ')

# Getting aspect ration
console.print(f'[bold cyan]Provide an aspect ration based on the intended font to be used. Larger values will make the ASCII art thinner, while lower values will make it wider. (default value is 0.5)[/bold cyan]')
console.print(f'[yellow]Valid inputs are greater than 0 and less than or equal to 1.[/yellow]')
aspect = float(input('Enter Value: '))

ascii_art = image_to_ascii(image, num_rows, model, aspect)

# Output
console.print(Rule('ASCII Art Generated'))
print(ascii_art)
        
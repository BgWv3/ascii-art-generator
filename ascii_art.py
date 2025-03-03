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
    file_path = filedialog.askopenfilename()
    return file_path

# Generating ASCII art
def image_to_ascii_row_height(image_path, row_hieght, model):
    img = Image.open(image_path).convert('L') # Grayscale
    original_width, original_height = img.size

    # Account for character aspect ratio
    char_aspect_ratio = 0.4 # Typical character is taller than wide

    # Calculate new width based on row height and aspect ratios
    new_height = row_hieght
    new_width = int(original_width / original_height * new_height / char_aspect_ratio)

    img = img.resize((new_width, new_height))

    ascii_models = {
        "detailed": (f"@%#*+=-:. "),

        "simple": (f"#*+-/\\|_ox"),

        "blocky": (f"█▓▒░#@%XO0"),

        "lined": (f"─│┌┐└┘├┤┬┴")
    }

    #ascii_chars = "@%#*+=-:. "
    ascii_chars = ascii_models[model]

    ascii_str = ""
    for y in range(new_height):
        for x in range(new_width):
            pixel = img.getpixel((x, y))
            char = ascii_chars[pixel // 25]
            ascii_str += char
        ascii_str += "\n"

    return ascii_str

console.print(Rule('Welcome to the ASCII Art Generator'))
image = get_file_path()
console.print(f'[bold cyan]What style would you like to create the ASCII art in? Please tye your selection[/bold cyan]')
console.print(f'[yellow]"detailed", "simple", "blocky", or "lined"[/yellow]')
model = input('Enter selection: ')
ascii_art = image_to_ascii_row_height(image, 20, model)
print(ascii_art)
        
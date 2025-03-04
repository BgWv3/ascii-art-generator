from fontTools.ttLib import TTFont
from rich.console import Console
from rich.table import Table

console = Console()

def get_font_metrics(font_path):
    # Load the font
    font = TTFont(font_path)

    # Access the 'hmtx' table for horizontal metrics
    hmtx = font['hmtx']

    # Access the 'head' table for font units per em
    units_per_em = font['head'].unitsPerEm

    # Get the advance width and left side bearing for a specific glyph (e.g., 'A')
    advance_width, left_side_bearing = hmtx['A']

    # Access the 'hhea' table for horizontal header
    hhea = font['hhea']

    # Get the ascent, descent, and line gap
    ascent = hhea.ascent
    descent = hhea.descent
    line_gap = hhea.lineGap

    # Calculate the total height
    total_height = (ascent - descent + line_gap) / units_per_em

    metrics = {
        'advance_width': advance_width / units_per_em,
        'left_side_bearing': left_side_bearing / units_per_em,
        'ascent': ascent / units_per_em,
        'descent': descent / units_per_em,
        'line_gap': line_gap / units_per_em,
        'total_height': total_height,
        'aspect_ratio': advance_width / total_height / units_per_em
    }

    table = Table(title="Font Metrics")

    table.add_column("Advanced Width")
    table.add_column("Left Side Bearing")
    table.add_column("Ascent")
    table.add_column("Descent")
    table.add_column("Line Gap")
    table.add_column("Total Height")
    table.add_column("Aspect Ratio")

    table.add_row(
            f"{metrics['advance_width']:.2f}",
            f"{metrics['left_side_bearing']:.2f}",
            f"{metrics['ascent']:.2f}",
            f"{metrics['descent']:.2f}",
            f"{metrics['line_gap']:.2f}",
            f"{metrics['total_height']:.2f}",
            f"{metrics['advance_width'] / metrics['total_height']:.2f}",
        )

    console.print(table)



# Example usage
font_path = 'fonts\FiraCodeNerdFontMono-Medium.ttf'
get_font_metrics(font_path)


import click
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_worksheet(filename, total_numbers, blanks):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    margin = 50  # 50px margin
    column_width = (width - 2 * margin) / 10
    row_height = 20  # Adjust as needed

    # Register a nice-looking font
    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

    rows = (total_numbers + 9) // 10
    numbers = list(range(1, total_numbers + 1))

    # Randomly replace digits with underscores
    blank_indices = []
    while len(blank_indices) < blanks:
        index = random.randint(0, total_numbers - 1)
        if index not in blank_indices and index - 1 not in blank_indices and index + 1 not in blank_indices:
            blank_indices.append(index)

    for index in blank_indices:
        numbers[index] = '_'

    # Draw the grid and numbers
    for row in range(rows):
        for col in range(10):
            index = row * 10 + col
            if index < total_numbers:
                x = margin + col * column_width
                y = height - margin - (row + 1) * row_height
                c.setFont('Vera', 14)  # Use the registered font
                if numbers[index] == '_':
                    c.setFillColor(HexColor('#ff0000'))  # Red for blanks
                else:
                    c.setFillColor(HexColor('#000000'))  # Black for numbers
                c.drawString(x + 5, y, str(numbers[index]))

    c.save()

@click.command()
@click.argument('total_numbers', type=int)
@click.argument('blanks', type=int)
def main(total_numbers, blanks):
    """
    Generates a PDF worksheet with a specified total number of digits.
    The worksheet is divided into 10 columns and a variable number of rows.
    A certain number of digits are replaced with underscores randomly.
    """
    if blanks > total_numbers:
        click.echo("Number of blanks cannot exceed total numbers.")
        return

    filename = "worksheet.pdf"
    create_worksheet(filename, total_numbers, blanks)
    click.echo(f"Worksheet created with {total_numbers} digits and {blanks} blanks.")

if __name__ == '__main__':
    main()
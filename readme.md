# PDF Worksheet Generator

This project is a Python script that generates a PDF worksheet with a specified total number of digits. The worksheet is divided into 10 columns and a variable number of rows. A certain number of digits are replaced with underscores randomly. The PDF is styled to be visually appealing and ensures that no two blanks are adjacent.

## Installation

1. Clone this repository cd into it.
2. Create a virtual env and activate

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required Python packages:

```bash
pip install reportlab click
```

4. Issue the command. This will create a pdf file named `worksheet.pdf` in the same folder.

```bash
python main.py  120 40
```

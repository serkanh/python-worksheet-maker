# PDF Worksheet Generator

The purpose of this project is to create a simple yet effective Python script that automates the generation of counting worksheets suitable for pre-K or kindergarten students. These worksheets are designed to help young learners practice their counting skills in an engaging and structured way.Python script  generates a PDF worksheet with a specified total number of digits. The worksheet is divided into 10 columns and a variable number of rows. A certain number of digits are replaced with underscores randomly. The PDF is styled to be visually appealing and ensures that no two blanks are adjacent.

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

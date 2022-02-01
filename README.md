# html2pdf
Python script to modify the content of some specific html files and convert them to pdf.

To install it: clone the repository, create a virtual environment for the script

and finally install the required libraries

Step 1 - git clone https://github.com/ramonVD/html2pdf.git

Step 2 - cd html2pdf

Step 3 - python3 -m venv env

Step 4 - source env/bin/activate

Step 5 - pip install -r requirements.txt

## Usage

Go to the script directory then type:

<code>python3 ioc_html2pdf.py **filename.html**</code>

To convert filename.html to pdf.

By default the output will be a file named outputX.pdf in the same directory (output.pdf or output{number} if the old filename already exists)

You can change the default filename by adding another parameter after filename.html. F.ex: python3 ioc_html2pdf.py index.html output_filename
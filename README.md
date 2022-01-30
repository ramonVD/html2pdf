# html2pdf
Python script to modify the content of some specific html files and convert them to pdf.

To use it, clone the repository then install the required libraries

Step 1 - git clone https://github.com/ramonVD/html2pdf.git

Step 2 - pip install -r requirements.txt

### Before using the script, you need to install the wkhtmltopdf binaries!

**Ubuntu**

If you're lucky (got all dependencies) you can try: <code>sudo apt-get install wkhtmltopdf</code>

If you're not, use these instructions: https://computingforgeeks.com/install-wkhtmltopdf-on-ubuntu-debian-linux/

or check the links below for precompiled binaries

**Windows/Mac**

If you're on windows or mac, last releases are here: 
https://wkhtmltopdf.org/downloads.html 

or here: https://github.com/wkhtmltopdf/wkhtmltopdf/releases/

## Usage

Go to the script directory then type:

<code>python3 ioc_html2pdf.py **convert_this_filename.html**</code>

By default the output will be a file named outputX.pdf in the same directory (output.pdf or output{number} if the old filename already exists
# html2pdf
Python script to modify the content of an html file and convert it to pdf. 

The applied changes to the html document converting it to pdf can be found in html_edits.py.

There are docker images available to use the script with the default parameters without having to install dependencies.

## Usage - Choose 1 of 2 (or both)

### - Using the python script

Installing the script/libraries:

**Step 1 -** git clone https://github.com/ramonVD/html2pdf.git

**Step 2 -** cd html2pdf

**Step 3 -** python3 -m venv env

**Step 4 -** source env/bin/activate

**Step 5 -** pip install -r requirements.txt

**Step 6 -** You'll need to install wkhtmltopdf if you don't have it (instructions are at the bottom of the page)

You can now go to the script directory and type:

<code>python3 ioc_html2pdf.py **filename.html**</code>

To convert filename.html to pdf.

By default the output will be a file named outputX.pdf in the same directory (output.pdf or output{number} if the old filename already exists)

You can change the default filename by adding another parameter after filename.html. F.ex: python3 ioc_html2pdf.py index.html output_filename


### - Using docker
The Docker image with the latest version is at https://hub.docker.com/repository/docker/ramonvd/pdfconvert, and probably other variations in the future.

Recommended way to do things is to execute html2pdf.sh to download and execute the latest image from docker automatically with the correct mounts, like this:

<code>./html2pdf.sh InputFilename.html (optional)OutputName</code>

(it's just a small bash script to call docker with the correct binds, feel free to check it but be careful with changing the mounts, the script is picky with the defaults, specially the input dir)

Keep in mind that by default the inputs need to be in the same directory you execute docker/the script from and the outputs will be generated into that same directory.


### If you're using the script and not the docker image, you need to install the wkhtmltopdf binaries!

**Ubuntu**

If you're lucky (got all dependencies) you can try: <code>sudo apt-get install wkhtmltopdf</code>

If you're not, use these instructions: https://computingforgeeks.com/install-wkhtmltopdf-on-ubuntu-debian-linux/

or check the links below for precompiled binaries

**Windows/Mac**

If you're on windows or mac, last releases are here: 
https://wkhtmltopdf.org/downloads.html 

or here: https://github.com/wkhtmltopdf/wkhtmltopdf/releases/

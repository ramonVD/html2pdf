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

### Normal script
Go to the script directory then type:

<code>python3 ioc_html2pdf.py **filename.html**</code>

To convert filename.html to pdf.

By default the output will be a file named outputX.pdf in the same directory (output.pdf or output{number} if the old filename already exists)

You can change the default filename by adding another parameter after filename.html. F.ex: python3 ioc_html2pdf.py index.html output_filename


### Using docker
The Docker image with the latest version is at https://hub.docker.com/repository/docker/ramonvd/pdfconver, and probably other variations in the future.

Reccomended way to do things is to execute html2pdf.sh to download and execute the latest image from docker automatically with the correct mounts, like this:

<code>./html2pdf.sh InputFilename.html (optional)OutputName</code>

(it's just a small bash script to call docker with the correct binds, feel free to check it but be careful with changing the mounts, the script is picky with the defaults, specially the input dir)

Keep in mind that the outputs will be in the same directory you execute docker/the script from.


### If you're using the script and not the docker image, you need to install the wkhtmltopdf binaries!

**Ubuntu**

If you're lucky (got all dependencies) you can try: <code>sudo apt-get install wkhtmltopdf</code>

If you're not, use these instructions: https://computingforgeeks.com/install-wkhtmltopdf-on-ubuntu-debian-linux/

or check the links below for precompiled binaries

**Windows/Mac**

If you're on windows or mac, last releases are here: 
https://wkhtmltopdf.org/downloads.html 

or here: https://github.com/wkhtmltopdf/wkhtmltopdf/releases/

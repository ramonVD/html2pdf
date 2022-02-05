FROM surnet/alpine-python-wkhtmltopdf:3.9.0-0.12.6-small

# Where the inputs will be found in the container
# Sync with the one used when using docker run
ENV INPUT_DIR="input"

WORKDIR /usr/src/html2pdf

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# For the tmp files used
VOLUME "/tmp/"

COPY . .

ENTRYPOINT ["python3", "ioc_html2pdf.py"]
# No default command CMD [...]

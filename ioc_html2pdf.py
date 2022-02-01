#!/usr/bin/env python
import sys
import datetime
import os
from tempfile import NamedTemporaryFile
from bs4 import BeautifulSoup
from DOMEditor.edit_html import edit_html
import pdfkit

# Shows messages about the actions taken by the program
VERBOSE = True

# Output files will be called thisX.pdf (f.ex: output1.pdf, output2.pdf...)
# unless specified otherwise
DEFAULT_OUTPUT_FILENAME = "output"
# Non changeable as of now
DEFAULT_OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

def printWTime(string):
    """Simple function to add the actual time to the start of a string"""
    print(datetime.datetime.now().strftime("%H:%M:%S") + " - " + string)

def is_valid_filename(filename):
    """Check if a file has a valid filename (valid chars and max length gotten from
    stack overflow and other sources, may be wrong)"""
    valid_chars = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if filename.length > 260:
        return "File path is too long"
    for char in filename:
        if char not in valid_chars:
            return "Filename contains illegal characters"
    return ""

def has_extension(string, ext):
    """Returns true/false if a string (supposedly a filename) has an extension or not.
    F.ex: index.html has_extension html -> True. hello.pdf has_extension txt -> False"""
    if (ext[0] != "."):
        ext = "." + ext
    if (string[-len(ext):] != ext):
        return False
    return True

def parse_args(args):
    """ Returns a dict with the input/output values, or an error key if there was an error.
    dict.inputs -> List with all the input names
    dict.output(optional) -> String with the desired output name
    dict.error(optional) -> String with an error message
    """
    data = {}
    if (len(args) < 2):
        data["error"] = """Please input a correct html file as the first argument. F.ex: python3 ioc_html2pdf.py filename.html"""
    else:
        inputs = [args[1].strip()] if len(args) == 2 else args[1:-1]
        # Inputs may be separated by commas instead of spaces
        if (len(inputs) == 1):
            inputs = inputs[0].split(",")
            for input in inputs[0]:
                input.strip()
        data["inputs"] = [input.strip() for input in inputs]
        if (len(args) > 2):
            data["output"] = args[-1]
    return data

class CouldntEditHtmlException(Exception):
    pass

# Specific output names are in, need to handle multiple inputs
def parse_document(args):
    parsed_args = parse_args(args)
    error_msg = ""
    if ("error" in parsed_args):
        error_msg = parsed_args["error"]
    else:
        for input in parsed_args["inputs"]:
            if not has_extension(input, "html"):
                error_msg = "Incorrect filename: %s - Input files need to have the html extension!" % input
                break
    if (len(error_msg) > 0):
        print(error_msg)
        return False

    # No support for multiple input filenames yet!
    filename = parsed_args["inputs"][0]

    modifiedSoup = ""
    if (not os.path.isdir(DEFAULT_OUTPUT_DIR)):
        try:
            os.mkdir(DEFAULT_OUTPUT_DIR)
        except OSError:
            print ("Cannot create output directory, please check directory permissions")
            return False

    # Output filename will have .pdf appended afterwards, remove it if it exists already
    # This will not check for weird output filenames, maybe apply is_valid_filename...
    final_default_output = os.path.join(DEFAULT_OUTPUT_DIR, DEFAULT_OUTPUT_FILENAME)
    if "output" in parsed_args:
        output_name = parsed_args["output"]
        if has_extension(output_name, "pdf"):
            final_default_output = os.path.join(DEFAULT_OUTPUT_DIR, output_name[:-4])
        else:
            final_default_output = os.path.join(DEFAULT_OUTPUT_DIR, output_name)

    output_filename = final_default_output

    counter = 1
    while (os.path.isfile(output_filename + ".pdf")):
        output_filename = final_default_output + str(counter)
        counter += 1
    output_filename += ".pdf"

    # Convert html file to bs4 object, and edit it
    try:
        with open(filename) as fp:
            soup = BeautifulSoup(fp, "html.parser")
            printWTime("Started editing html elements.") if (VERBOSE) else None
            modifiedSoup = edit_html(soup)
            printWTime("Finished editing html elements.") if (VERBOSE) else None
    except IOError:
        print("File %s is not accessible" % filename)
        return False

    # Convert bs4 object to pdf and write it to file
    try:
        with NamedTemporaryFile(mode="w+t", suffix=".html") as fp:
            if (modifiedSoup == ""):
                raise CouldntEditHtmlException("Unable to parse html from: %s" % filename)
            fp.write(str(modifiedSoup))
            try:
                printWTime("Starting html to pdf conversion...") if (VERBOSE) else None
                pdfkit.from_file(fp.name, output_filename)
                printWTime("""Finished html to pdf conversion.
Output file is at %s""" %output_filename) if (VERBOSE) else None
                return True
            except Exception as e:
                print("Error while converting to pdf: %s" % str(e))
                print("Check output file at %s" % output_filename)

    except IOError:
        print("""Could not create temporal file, check directory permissions""")
    except CouldntEditHtmlException as err:
        print(err)
    return False


if __name__ == '__main__':
    parse_document(sys.argv)



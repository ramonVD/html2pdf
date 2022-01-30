#!/usr/bin/env python
import sys
import pdfkit
import datetime
import os
from tempfile import NamedTemporaryFile
from bs4 import BeautifulSoup
from edit_html import edit_html

# Shows messages about the actions taken by the program
VERBOSE = True

#Output files will be called thisX.pdf (f.ex: output1.pdf, output2.pdf...)
DEFAULT_OUTPUT_FILENAME = "output"

def printWTime(string):
    """Simple function to add the actual time to the start of a string"""
    print(datetime.datetime.now().strftime("%H:%M:%S") + " - " + string)


def parse_document(args):
    if (len(args) > 1):
        filename = args[1]
        modifiedSoup = ""
        output_filename = DEFAULT_OUTPUT_FILENAME
        counter = 1
        while (os.path.isfile(output_filename + ".pdf")):
            output_filename = DEFAULT_OUTPUT_FILENAME + str(counter)
            counter += 1
        output_filename += ".pdf"
        try:
            with open(filename) as fp:
                soup = BeautifulSoup(fp, "html.parser")
                printWTime("Started editing html elements.") if (VERBOSE) else None
                modifiedSoup = edit_html(soup)
                printWTime("Finished editing html elements.") if (VERBOSE) else None
        except IOError:
            print("File %s not accessible" % filename)
            return False
        
        try:
            with NamedTemporaryFile(mode="w+t",
                            dir="./", suffix=".html") as fp:
                if (modifiedSoup == ""):
                    raise Exception("Unable to parse html from: %s" % filename)
                fp.write(str(modifiedSoup))
                try:
                    printWTime("Starting html to pdf conversion...") if (VERBOSE) else None
                    pdfkit.from_file(fp.name, output_filename)
                    # Change this in the future to handle multiple inputs, specific output names, etc
                    printWTime("""Finished html to pdf conversion.
Output file is named %s""" %output_filename) if (VERBOSE) else None
                    return True
                except Exception as e:
                    print("Error while converting to pdf: %s" % str(e))
                    print("Check output file at %s" % output_filename)
                
        except IOError:
            print("""Could not create temporal file, check directory permissions""")
        except Exception as err:
            print("uhhh", err)
        return False

    else:
        print("""Please input a correct html file as the argument. F.ex: python3 main.py filenameHere""")
        return False

if __name__ == '__main__':
    parse_document(sys.argv)

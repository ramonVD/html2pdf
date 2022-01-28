#!/usr/bin/env python
import sys
import pdfkit
import datetime
import os
from tempfile import NamedTemporaryFile
from bs4 import BeautifulSoup

# Shows messages about the actions taken by the program
VERBOSE = True

BODY_FONT_SIZE = "1.1em"
TAB_MARGIN_BOTTOM = "15px"
TAB_PADDING_BOTTOM = "10px"
TAB_BORDER_BOTTOM = "2px solid black"


def clean_html(soup):
    """!Mutates! the html contents of a bs4 object
    (itself a parse of an html page).
    So far it only adds some stylings to elements
    that would convert poorly to pdf
    without the changes.

    Args:
        soup ([Bs4Object]): bs4 object that contains
        the html that's gonna be parsed and modified

    Returns:
        [soup]: bs4 object after the modifications to
        its html content
    """

    body = soup.body
    # Change body font size
    body["style"] = "font-size:{};".format(BODY_FONT_SIZE)

    collapsables = soup.find_all(attrs={"class", 'collapse'})
    # Stop hiding collapsables insides
    for collapsable in collapsables:
        assign_attributes(collapsable, style="display:block;")

    tabsContainers = soup.find_all(attrs={"class", 'tab-content'})
    tabStyle = """display:block; opacity:1; margin-bottom:{mb};
    padding-bottom:{pb}; border-bottom:{bb};""".format(
        mb=TAB_MARGIN_BOTTOM, pb=TAB_PADDING_BOTTOM, bb=TAB_BORDER_BOTTOM)
    for tabContainer in tabsContainers:
        # Show all tabs in a tab container (normally only one is shown)
        tabs = list(filter(lambda x: len(x) > 0,
                           tabContainer.find_all(attrs={"class", 'tab-pane'})))
        for tab in tabs:
            assign_attributes(tab, style=tabStyle)
    return soup


def assign_attributes(object, **kwargs):
    """Assigns an arbitray amount of key / values to an object.
    Intented use is to add attributes to an html tag in a bs4 object.

    Args:
        object: any bs4 object containing an html element.
        intented args should be in the form key=value
        f.ex: assign_attributes(htmlTag, style='font-size:35px;')
    """
    for key in kwargs:
        object[key] = kwargs[key]


def printWTime(string):
    """Simple function to add the actual time to the start of a string"""
    print(datetime.datetime.now().strftime("%H:%M:%S") + " - " + string)


def parse_document(args):
    if (len(args) > 1):
        filename = args[1]
        modifiedSoup = ""
        try:
            with open(filename) as fp:
                soup = BeautifulSoup(fp, "html.parser")
                printWTime("Started cleaning html elements.") if (VERBOSE) else None
                modifiedSoup = clean_html(soup)
                printWTime("Finished cleaning html elements.") if (VERBOSE) else None
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
                    pdfkit.from_file(fp.name, 'output.pdf')
                    printWTime("Finished html to pdf conversion.") if (VERBOSE) else None
                    return True
                except Exception as e:
                    print("Error while converting to pdf: %s" % str(e))

        except IOError:
            print("""Could not create temporal file, check directory permissions""")
        except Exception as err:
            print(err)
        return False

    else:
        print("""Please input a correct html file as the argument. F.ex: python3 main.py filenameHere""")
        return False

if __name__ == '__main__':
    parse_document(sys.argv)

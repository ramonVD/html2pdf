import datetime
import re


def printWTime(string):
    """Simple function to add the actual time to the start of a string"""
    print(datetime.datetime.now().strftime("%H:%M:%S") + " - " + string)


def is_valid_filename(filename):
    """Check if a file has a valid filename (valid chars and max length gotten from
    stack overflow and other sources, may be wrong)"""
    # Added some accents, ö and stuff like that is still verboten
    valid_chars = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789àèéíóòúüÀÈÉÍÒÓÚÜ'
    if len(filename) > 260:
        return False
    for char in filename:
        if char not in valid_chars:
            return False
    return True


def has_extension(string, ext):
    """Returns true/false if a string (supposedly a filename) has an extension or not.
    F.ex: index.html has_extension html -> True. hello.pdf has_extension txt -> False"""
    if (ext[0] != "."):
        ext = "." + ext
    if (string[-len(ext):] != ext):
        return False
    return True


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


"""Changes relative src/href for the absolute path in the filesystem,
used because wkhtmltopdf doesnt like importing relative stuff.
Base_path is obtained from the function calling this one.
Created to fix something that isnt broken (at least so far), so unused"""


def absolutize_url_paths(soup, base_path):
    all_path_elements = soup.find_all(href=True) + soup.find_all(src=True)
    non_url_non_svg = '^(?!http|data:)'
    for element in all_path_elements:
        if (has_attr(element, "src")):
            element["src"] = re.sub(non_url_non_svg, base_path, element["src"])
        elif (has_attr(element, "href")):
            element["href"] = re.sub(
                non_url_non_svg, base_path, element["href"])
    return soup


"""Helper function, it does what hasattr should for bs4 objects.
Just check if the desired attribute exists in an object."""


def has_attr(object, attr):
    try:
        object[attr]
        return True
    except:
        return False

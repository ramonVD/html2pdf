
BODY_FONT_SIZE = "1.1em"
TAB_MARGIN_BOTTOM = "15px"
TAB_PADDING_BOTTOM = "10px"
TAB_BORDER_BOTTOM = "2px solid black"


def edit_html(soup):
    """!Mutates! the html contents of a bs4 object
    (itself a parse of an html page).
    So far it only adds some stylings to elements
    that would convert poorly to pdf
    without the changes.
    
    Add more stylings and changes here as needed

    Args:
        soup ([Bs4Object]): bs4 object that contains
        the html that's gonna be parsed and modified

    Returns:
        [soup]: bs4 object after the modifications to
        its html content
    """
    
    # Change body font size
    body = soup.body
    body["style"] = "font-size:{};".format(BODY_FONT_SIZE)

    # Stop hiding the insides of collapsables. May conflict with old collapsables
    collapsables = soup.find_all(attrs={"class", 'collapse'})
    for collapsable in collapsables:
        assign_attributes(collapsable, style="display:block;")

    # Show all tabs in a tab container (normally only one is shown)
    tabs_containers = soup.find_all(attrs={"class", 'tab-content'})
    tab_style = """display:block; opacity:1; margin-bottom:{mb};
    padding-bottom:{pb}; """.format(
        mb=TAB_MARGIN_BOTTOM, pb=TAB_PADDING_BOTTOM)
    for tab_container in tabs_containers:
        tabs = list(filter(lambda x: len(x) > 0,
                           tab_container.find_all(attrs={"class", 'tab-pane'})))
        tab_counter = 0
        tab_final_style = tab_style
        for tab in tabs:
            # Do not add a black bottom border to the last tab in the pane
            if (tab_counter < len(tabs) - 1):
                tab_final_style = tab_style + "border-bottom: %s" % TAB_BORDER_BOTTOM
            else:
                tab_final_style = tab_style
            assign_attributes(tab, style=tab_final_style)
            tab_counter += 1
            
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

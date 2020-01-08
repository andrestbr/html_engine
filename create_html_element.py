'''Creates an html element.

Args:
    element (str): element name to be created, i.e. <div>
    
    content_list (str): the content of the element <div>'content'</div>
        
    attribute (str) (optional): for creating an element with an attribute <div style='text-align:right'>'content'</div>

    attribute_value (str) (optional): value for the attribute

Returns:
    html element

'''


def create_html_element(element, content_list, attribute=False):
    
    # convert the content (a list of elements) in a string
    list = ''
    for e in content_list:
        list = list + e
    
    # build the html element and store it in a variable
    html_element = '<' + element + '>' + list + '</' + element + '>'

    # if an attribute and a value are given, build the html element with an attribute (style='text-align:right') and store it in a variable
    if attribute:
        attribute_length = len(attribute)
        attribute_number = 1
            
        attributes = 'style="'

        for k, v in attribute.items():
            attributes = attributes + k + ':' + v

            if attribute_number == attribute_length:
                attributes = attributes + '"'

            else:
                attributes = attributes + ';'
        
            attribute_number = attribute_number + 1
        
        html_element = '<' + element + ' ' + attributes + '>' + list + '</' + element + '>'

    return html_element

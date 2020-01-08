from create_html_element import create_html_element

td = create_html_element('td', 'value', {'text-align':'right', 'background-color':'blue'})
print(td)

td = create_html_element('td', 'value', {'text-align':'right'})
print(td)

tr = create_html_element('tr', td)
print(tr)

table = create_html_element('table', tr)
print(table)

print(create_html_element('td', ''))

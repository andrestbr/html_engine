from get_headers_list import get_headers_list
from add_headers_list import add_headers_list

b = [["DW News","DW Deutsch","DW Global Ideas"],["1655868","366335","375110"],["1665925","367071","377462"]]
c = [["DW News","1655868","1665925"],["DW Deutsch","366335","367071"],["DW Global Ideas","375110","377462"]]

headers = ['Facebook Account', 'letzte Woche', 'diese Woche']

print(add_headers_list(b, headers, transposed=False))
print(add_headers_list(c, headers))

print(get_headers_list(b, transposed=True))
print(get_headers_list(c))
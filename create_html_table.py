import csv
import pandas as pd

from dashboard.html_engine.create_html_element import create_html_element
from dashboard.html_engine.check_align import check_align
from dashboard.html_engine.get_headers_list import get_headers_list

'''Create an html table.

Args:


'''


# creates an html table
# returns a table
#
# arguments:
#
# file: file with the data in csv format
#
# DW News;1655868;1665925
# DW DE;366335;367071;736
# DW Global Ideas;375110;377462
#
# structure:
#
# table.tr.th 
# table.tr.td


def create_html_table(file, transposed=True):
    
    with open(file, encoding='utf-8') as csv_file:
        fans = csv.reader(csv_file, delimiter=';')
        fans2 = pd.read_csv(filepath_or_buffer=file, sep=';')        

        
        # store the rows as lists
        fans_list = list(fans)
        
        print(fans_list)
        print(fans2)

        # replaced by headers2?
        headers = get_headers_list(fans_list, transposed=True)
        #headers2 = fans2.columns.values

        print(headers)
        
        # create table
        
        # create headers for the table
        
        # create a list for the headers
        th_list = list()
        
        # create the headers
        for i in headers:
            # create a th html element
            th_element = create_html_element('th', i)
            th_list.append(th_element)
            
            # create a row from the headers
            tr_th = create_html_element('tr', th_list)
        
        # create a list for the rows (as tr html elements)
        tr_list = list()
        
        # add the headers to the rows list
        tr_list.append(tr_th)
        
        # create tr html elements
        
        # [1: ] ignore the first elements of the first rows as they are already used als headers
        for i in fans_list[1: ]:

            # create a list for the elements of the rows (as td html elements)
            td_list = list()

            # create td html elements
            for j in i:
                
                # check if the value is a digit or a percent number and add the attribute alight right
                if check_align(j):
                    j = '<pre>' + j + '</pre> '
                    td_element = create_html_element('td', j, {'text-align':'right'})
                else:
                    td_element = create_html_element('td', j)	

                td_list.append(td_element)
            
            tr_element = create_html_element('tr', td_list)
            
            tr_list.append(tr_element)
            
        # create html table
        html_table = create_html_element('table', tr_list)
        
        
    return html_table

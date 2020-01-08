def get_headers_list(list_source, transposed=False):
	
	if transposed:
		headers = list_source[0]

	else:
		headers = list()
	
		for i in list_source:
			headers.append(i[0])
		
	return headers



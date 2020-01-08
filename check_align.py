# checks if the string should be right aligned

def check_align(string):
	if 'NA' in string:
		return True

	if '%' in string:
		return True
	
	if '<code>' in string:
		return True

	try:
		float(string)
		return True
	except:
		pass 

	try:
		float(string.replace(',', '.'))
		return True
	except:
		pass
	try:
		float(string.replace('.', ''))
		return True
	except:
		pass

	else:
		return False





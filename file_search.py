def read(filename):
	"""
	Reads a text file and returns its content
	"""
	with open(filename) as f:
		content = f.read()
	return content


def search_text_in_file(text, filename):
	"""
	Reads a file and returns the number of occurrences of text
	"""
	occurrences = 0
	file_content = read(filename)
	occurrences += file_content.count(text)
	return occurrences

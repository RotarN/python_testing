

def custom_sum(*args):
	result = 0
	for arg in args:
		if isinstance(arg, (list, tuple)):
			result += custom_sum(*arg)
		else:
			try:
				converted = float(arg)
				result += converted
			except ValueError:
				raise TypeError("unsupported object of type: {}".format(type(arg)))
	return result

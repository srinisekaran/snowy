import time 

def time_track(func):
	def wrapper(*args, **kwargs):
		time_init = time.time()
		result = func(*args, **kwargs)
		elapsed_time = time.time() - time_init
		print('function [{}] finished in {} ms'.format(
			func.__name__, (elapsed_time * 1000)))
		return result
	return wrapper 
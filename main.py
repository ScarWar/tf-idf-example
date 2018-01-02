import math
from collections import Counter


def raw_count(t, d):
	return d.count(t)


def count_words(d):
	return len(d.split())


def log_scale_freq(t, d, f):
	return math.log(1 + f)


def get_occure_list(d):
	return Counter((d.split()))


def get_max_freq(d):
	occure_list = get_occure_list(d)
	return max(occure_list.items(),
			   key=lambda t: t[1])[1] \
		/ sum(occure_list.values())


def augmented_freq(t, d, f):
	ftf_prime = get_max_freq(d)
	return (1 + f / ftf_prime) / 2


def tf(t, d):
	num_of_words = count_words(d)
	f_term_freq = raw_count(t, d) / num_of_words
	return f_term_freq


def main():
	terms = [
		'love',
		'death',
		'life'
	]
	weight_fucntions = [
		('ID', lambda t, d, f: f),
		('Log Scale freq', lambda t, d, f: log_scale_freq(t, d, f)),
		('Augmented freq', lambda t, d, f: augmented_freq(t, d, f))
	]
	with open("romeo-juliet.txt", 'r') as f:
		text = f.read()
		for func_name, func in weight_fucntions:
			print('=================', func_name)
			for t in terms:
				tft = tf(t, text)
				print('terms: %s\ttf:\t%.10f' % (t, func(t, text, tft)))
			print()

if __name__ == '__main__':
	main()

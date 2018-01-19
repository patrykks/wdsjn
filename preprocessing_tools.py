import csv
import re
from file_processor import process_file_by_line, process_file_by_word

def process(input_filename, output_filename, polimorf_dict, stop_words, step_1_filename='step_1.txt', step_2_filename='step_2.txt', step_3_filename='step_3.txt'):
    print('Step 1 - Remove non-white space, non alpha-numeric characters - start')
    fn = lambda x: remove_non_white_space_non_alphanumeric_characters(x)
    process_file_by_line(input_filename, fn, step_1_filename)

    print('Step 2 - Convert to lower case - start')
    fn = lambda x: x.lower()
    process_file_by_word(step_1_filename, fn, step_2_filename)

    print('Step 3 - Transform to simple form - start')
    fn = lambda x: dictionary_form_of_word(polimorf_dict, x)
    process_file_by_word(step_2_filename, fn, step_3_filename)

    print('Step 4 - Remove stop words - start')
    fn = lambda x: remove_stop_words(stop_words, x)
    process_file_by_word(step_3_filename, fn, output_filename)

def initialize_polimorf_dict(polimorf_dict_filename):
	polimorf_dict = {}

	f = open(polimorf_dict_filename, 'r')
	csv_reader = csv.reader(f)

	for row in csv_reader:
		polimorf_dict[row[0]] = row[1]

	return polimorf_dict

def remove_non_white_space_non_alphanumeric_characters(text):
	pattern = re.compile('[^\sa-zA-ZĄĆĘŁŃÓŚŹŻĆąćęłńóśźż0-9]+')

	return pattern.sub('', text)

def dictionary_form_of_word(polimorf_dict, word):
	return polimorf_dict.get(word, word)

def remove_stop_words(stop_word_list, word):
    if word in stop_word_list:
        return ''
    return word





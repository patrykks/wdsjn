import csv
from nltk.tokenize import word_tokenize

def lemmatize(tokens, polimorf_dict_name):
	polimorf_dict = initialize_polimorf_dict(polimorf_dict_name)

	return [ dictionary_form_of_word(polimorf_dict, token) for token in tokens ]

def convert_to_lower_case(simple_forms):
	return [ simple_form.lower() for simple_form in simple_forms]

def compute_words_occurrence_frequency(simple_forms):
	ocurrences = {}

	for word in simple_forms:
		number_occurences_of_word = ocurrences.get(word, 0)
		ocurrences[word] = number_occurences_of_word + 1

	return ocurrences

def compute_words_cooccurence_frequency(simple_forms, stimus_words, window_width):
	cooccurences = {}

	for i in range(len(simple_forms)):
		if simple_forms[i] in stimus_words:
			window = define_window_for_word(simple_forms, i, window_width)
			for coelement in window:
				form_coocurence = cooccurences.get(simple_forms[i], {})
				coelement_frequency = form_coocurence.get(coelement, 0)
				form_coocurence[coelement] = coelement_frequency + 1
				cooccurences[simple_forms[i]] = form_coocurence

	return cooccurences


def initialize_polimorf_dict(polimorf_dict_name):
	polimorf_dict = {}

	f = open(polimorf_dict_name, 'r')
	csv_reader = csv.reader(f)

	for row in csv_reader:
		polimorf_dict[row[0]] = row[1]

	return polimorf_dict

def dictionary_form_of_word(polimorf_dict, word):
	return polimorf_dict.get(word, word)

def define_window_for_word(simple_forms, i, window_width):
	left_side_start=max(0, i - window_width)
	left_side_end= max(i - 1, 0)

	right_side_start= min(i + 1, len(simple_forms) )
	right_side_end = min(i + window_width, len(simple_forms))

	return simple_forms[left_side_start:left_side_end] + simple_forms[right_side_start:right_side_end] 

corpa_filename = 'data/korpus-pan-100.txt'
polimorf_dict_name = 'data/PoliMorf-0.6.7.tab'
window_width = 12
stimus_words = ['samochód', 'samolot', 'góra', 'dom', 'budynek']

corpa_file = open(corpa_filename, "r", encoding="utf-8")
corpa_file_content = corpa_file.read()
tokens = word_tokenize(corpa_file_content)
simple_forms = lemmatize(tokens, polimorf_dict_name)
simple_forms  = convert_to_lower_case(simple_forms)

ocurrences = compute_words_occurrence_frequency(simple_forms)
cooccurences = compute_words_cooccurence_frequency(simple_forms, stimus_words, window_width)

#print(simple_forms)
#print(ocurrences)
print(cooccurences)


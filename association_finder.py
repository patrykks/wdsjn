import csv
import pprint
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

def compute_associations_strengths_coefficients(cooccurences, ocurrences, alpha, beta, gamma, Q):
	associations = {}

	for stimus_words in cooccurences.keys():
		formula_limit = beta * Q
		for coresponding_word in cooccurences[stimus_words]:
			if (ocurrences[stimus_words] > formula_limit):
				print('Frequent word:', coresponding_word, ocurrences[stimus_words], formula_limit)
				association_coefficient = compute_association_strengths_for_frequent_words(
											cooccurences[stimus_words][coresponding_word],
											ocurrences[coresponding_word],
											alpha
										)
			else:
				print('Rare word:', coresponding_word, ocurrences[stimus_words], formula_limit)
				association_coefficient = compute_association_strengths_for_rare_words(
											cooccurences[stimus_words][coresponding_word],
											gamma,
											Q
										)
			
			associations_for_stimus_word = associations.get(stimus_words, {})
			associations_for_stimus_word[coresponding_word] = association_coefficient
			associations[stimus_words] = associations_for_stimus_word

	return associations

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

def compute_association_strengths_for_frequent_words(frequency_of_coocurence, frequency_of_single_word, alpha):
	return frequency_of_coocurence / (frequency_of_single_word ** alpha)

def compute_association_strengths_for_rare_words(frequency_of_coocurence, gamma, Q):
	return frequency_of_coocurence / (gamma * Q)

pp = pprint.PrettyPrinter()

corpa_filename = 'data/korpus-pan-100.txt'
polimorf_dict_name = 'data/PoliMorf-0.6.7.tab'
window_width = 12
stimus_words = ['samochód', 'samolot', 'góra', 'dom', 'budynek']

alpha = 0.66
beta = 0.00002
gamma = 0.00002

corpa_file = open(corpa_filename, "r", encoding="utf-8")
corpa_file_content = corpa_file.read()
tokens = word_tokenize(corpa_file_content)
simple_forms = lemmatize(tokens, polimorf_dict_name)
simple_forms  = convert_to_lower_case(simple_forms)

ocurrences = compute_words_occurrence_frequency(simple_forms)
cooccurences = compute_words_cooccurence_frequency(simple_forms, stimus_words, window_width)
associations = compute_associations_strengths_coefficients(
					cooccurences,
					ocurrences,
					alpha,
					beta,
					gamma,
					len(simple_forms)
				)


#print(simple_forms)
#print(ocurrences)
#print(cooccurences)
pp.pprint(associations)

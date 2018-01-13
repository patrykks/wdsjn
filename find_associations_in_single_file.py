import os
import json
from association_finder import  freqDist, compute_words_cooccurence_frequency_from_file, compute_associations_strengths_coefficients

preprocessed_input_file = 'preprocessed-korpus-pan-10000.txt'
input_data_tag = 'korpus-pan'
stimus_words = ['karabin', 'kula', 'wojsko', 'żołnierz']
min_number_of_occurences = 10
number_of_printed_associations = 30
window_width = 12

alpha = 0.66
beta = 0.00002
gamma = 0.00002

ocurrences = {}
cooccurences = {}

print('Compute occurences')
freqDist(ocurrences, preprocessed_input_file)

print('Compute coocurences')
compute_words_cooccurence_frequency_from_file(cooccurences, preprocessed_input_file, ocurrences, stimus_words, window_width, min_number_of_occurences)

print('Compute associations')
associations = compute_associations_strengths_coefficients(
					cooccurences,
					ocurrences,
					alpha,
					beta,
					gamma,
					sum(ocurrences.values()))

for stimus_word in stimus_words:
	output_filename = 'data/' + input_data_tag + '_' + stimus_word + '.json'
	with open(output_filename, 'w') as fp:
		json.dump(associations[stimus_word], fp, ensure_ascii=False)

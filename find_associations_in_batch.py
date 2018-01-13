import os
import json
from association_finder import  freqDist, compute_words_cooccurence_frequency_from_file, compute_associations_strengths_coefficients

rootDir = 'data/preprocessed_pap-all'
input_data_tag = 'pap-all'
window_width = 12
stimus_words = ['karabin', 'kula', 'wojsko', 'żołnierz']
min_number_of_occurences = 10
number_of_printed_associations = 30

alpha = 0.66
beta = 0.00002
gamma = 0.00002

ocurrences = {}
cooccurences = {}

print('Compute occurences')
for dirName, subdirList, fileList in os.walk(rootDir):
	print(dirName)
	for fname in fileList:
		input_filename = os.path.join(dirName, fname)
		freqDist(ocurrences, input_filename)

print('Compute coocurences')
for dirName, subdirList, fileList in os.walk(rootDir):
	print(dirName)
	for fname in fileList:
		input_filename = os.path.join(dirName, fname)
		compute_words_cooccurence_frequency_from_file(cooccurences, input_filename, ocurrences, stimus_words, window_width, min_number_of_occurences)


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

def freqDist(ocurrences, input_filename):
	with open(input_filename) as input_file:
		for line in input_file:
			for word in line.split():
				ocurrences[word] = ocurrences.get(word, 0) + 1

def compute_words_cooccurence_frequency_from_file(cooccurences ,input_filename, ocurrences, stimus_words, window_width, min_number_of_occurences):
	with open(input_filename) as input_file:
		left_side = []
		for line in input_file:
			word_list = left_side + line.split()
			compute_words_cooccurence_frequency_from_list(word_list, ocurrences, stimus_words, window_width, min_number_of_occurences, cooccurences)
			left_side = word_list[-window_width:]

def compute_words_cooccurence_frequency_from_list(simple_forms, ocurrences, stimus_words, window_width, min_number_of_occurences, cooccurences):
	for i in range(len(simple_forms)):
		if simple_forms[i] in stimus_words:
			window = define_window_for_word(simple_forms, i, window_width)
			for coelement in window:
				if ocurrences[coelement] >= min_number_of_occurences:
					form_coocurence = cooccurences.get(simple_forms[i], {})
					coelement_frequency = form_coocurence.get(coelement, 0)
					form_coocurence[coelement] = coelement_frequency + 1
					cooccurences[simple_forms[i]] = form_coocurence

def compute_associations_strengths_coefficients(cooccurences, ocurrences, alpha, beta, gamma, Q):
	associations = {}
	formula_limit = beta * Q

	for stimus_words in cooccurences.keys():
		for coresponding_word in cooccurences[stimus_words]:
			if (ocurrences[stimus_words] > formula_limit):
				#print('Frequent word:', coresponding_word, Q, ocurrences[coresponding_word], formula_limit)
				association_coefficient = compute_association_strengths_for_frequent_words(
											cooccurences[stimus_words][coresponding_word],
											ocurrences[coresponding_word],
											alpha
										)
			else:
				#print('Rare word:', Q,  coresponding_word, ocurrences[coresponding_word], formula_limit)
				association_coefficient = compute_association_strengths_for_rare_words(
											cooccurences[stimus_words][coresponding_word],
											gamma,
											Q
										)

			associations_for_stimus_word = associations.get(stimus_words, {})
			associations_for_stimus_word[coresponding_word] = association_coefficient
			associations[stimus_words] = associations_for_stimus_word

	return associations

def compute_association_strengths_for_frequent_words(frequency_of_coocurence, frequency_of_single_word, alpha):
	return frequency_of_coocurence / (frequency_of_single_word ** alpha)

def compute_association_strengths_for_rare_words(frequency_of_coocurence, gamma, Q):
	return frequency_of_coocurence / (gamma * Q)

def define_window_for_word(simple_forms, i, window_width):
	left_side_start=max(0, i - window_width)
	left_side_end= max(i - 1, 0)

	right_side_start= min(i + 1, len(simple_forms) )
	right_side_end = min(i + window_width, len(simple_forms))

	return simple_forms[left_side_start:left_side_end] + simple_forms[right_side_start:right_side_end]

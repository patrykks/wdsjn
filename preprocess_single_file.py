from nltk.corpus import stopwords
from preprocessing_tools import initialize_polimorf_dict, process

if __name__ == "__main__":
    polimorf_dict_filename = 'data/PoliMorf-0.6.7.tab'
    polimorf_dict = initialize_polimorf_dict(polimorf_dict_filename)
    stop_words = stopwords.words('polish')
    input_filename = 'data/korpus-pan.txt'

    output_filename = 'data/preprocessed-korpus-pan.txt'

    process(input_filename, output_filename, polimorf_dict, stop_words)


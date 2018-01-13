import os
from nltk.corpus import stopwords
from preprocessing_tools import initialize_polimorf_dict, process

rootDir = 'data/pap-all'
polimorf_dict_filename = 'data/PoliMorf-0.6.7.tab'
polimorf_dict = initialize_polimorf_dict(polimorf_dict_filename)
stop_words = stopwords.words('polish')


for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        input_filename = os.path.join(dirName, fname)

        output_filename = os.path.join(dirName, fname).replace("pap-all", "preprocessed_pap-all")

        print(input_filename, ",", output_filename)

        os.makedirs(dirName.replace("pap-all", "preprocessed_pap-all"), exist_ok=True)

        process(input_filename, output_filename, polimorf_dict, stop_words)

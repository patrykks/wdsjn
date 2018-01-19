import json
import pprint

pp = pprint.PrettyPrinter()
number_of_assocation_to_print = 30
association_coefficients_filename = '../data/kula.json'
keyword = 'kula'

def print_association(keyword, number_of_assocation_to_print, associations):
    print('----------------------------------------------')
    print(keyword)
    print('----------------------------------------------')
    pp.pprint(sorted(associations.items(), key=lambda x:x[1], reverse=True)[:number_of_assocation_to_print])

if __name__ == "__main__":
    with open(association_coefficients_filename) as json_result:
        associations = json.load(json_result)
        print_association(keyword, number_of_assocation_to_print, associations)

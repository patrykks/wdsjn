import json
import csv
import itertools as it
from collections import OrderedDict

def read_from_json(filename):
    return json.load(open(filename), object_pairs_hook=OrderedDict)

def read_from_csv(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        result = OrderedDict()
        for row in reader:
            result[row[1].lower()] = int(row[0])
    return result

def sorted_list_with_n_tuples_containing_biggest_values(old_dict, n):
    return sorted(old_dict.items(), key=lambda x:x[1], reverse=True)[:n]

def convert_list_of_tuples_to_list_of_ranks(sorted_list):
    new_list = []
    rank = 0
    for item in sorted_list:
        elem = list(item)
        elem[1] = rank
        new_list.append(elem)
        rank += 1
    return new_list

def sum_differences_of_positions(base_dict, compared_dict):
    sum = 0
    n = len(base_dict)

    for key, value in base_dict.items():
        if key in compared_dict:
            #print('Common value:', key,":",abs(value - compared_dict[key]))
            sum += abs(value - compared_dict[key])
        else:
            #   print(key,":",n)
            sum += n

    return sum

def compute_sum_of_positions_differences(base_dict, compared_dict):
    base_n_best_match_sorted = sorted_list_with_n_tuples_containing_biggest_values(base_dict, number_of_elements)
    compared_n_best_match_sorted = sorted_list_with_n_tuples_containing_biggest_values(compared_dict, number_of_elements)

    base_dict_of_ranks = OrderedDict(convert_list_of_tuples_to_list_of_ranks(base_n_best_match_sorted))
    compared_dict_of_ranks = OrderedDict(convert_list_of_tuples_to_list_of_ranks(compared_n_best_match_sorted))

    return sum_differences_of_positions(base_dict_of_ranks, compared_dict_of_ranks)


if __name__ == "__main__":
    number_of_elements = 30

    dict_of_results = {}

    dict_of_results['pap_all-kula'] = read_from_json('results/pap-all_kula.json')
    dict_of_results['pap_all-karabin'] = read_from_json('results/pap-all_kula.json')
    dict_of_results['pap_all-zolnierz'] = read_from_json('results/pap-all_żołnierz.json')
    dict_of_results['pap_all-wojsko'] = read_from_json('results/pap-all_wojsko.json')

    dict_of_results['wiki-kula'] = read_from_json('results/wiki_kula.json')
    dict_of_results['wiki-karabin'] = read_from_json('results/wiki_kula.json')
    dict_of_results['wiki-zolnierz'] = read_from_json('results/wiki_żołnierz.json')
    dict_of_results['wiki-wojsko'] = read_from_json('results/wiki_wojsko.json')
    
    dict_of_results['korpus_pan-kula'] = read_from_json('results/korpus-pan_kula.json')
    dict_of_results['korpus_pan-karabin'] = read_from_json('results/korpus-pan_kula.json')
    dict_of_results['korpus_pan-zolnierz'] = read_from_json('results/korpus-pan_żołnierz.json')
    dict_of_results['korpus_pan-wojsko'] = read_from_json('results/korpus-pan_wojsko.json')

    dict_of_results['ref-kula'] = read_from_csv('results/kula.csv')
    dict_of_results['ref-wojsko'] = read_from_csv('results/wojsko.csv')
    dict_of_results['ref-zolnierz'] = read_from_csv('results/zolnierz.csv')
    dict_of_results['ref-karabin'] = read_from_csv('results/karabin.csv')

    combinations = list(it.combinations(dict_of_results.keys(), 2))
    for combination in combinations:
        if (combination[0].split('-')[1] == combination[1].split('-')[1]):
            print("combination of:", combination[0], ",", combination[1])
            print(compute_sum_of_positions_differences(dict_of_results[combination[0]], dict_of_results[combination[1]]))


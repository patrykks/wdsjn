import json
import csv
from collections import OrderedDict
import networkx as nx

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

def add_associations(G, keyword, associations):
    if not G.has_node(keyword):
        G.add_node(keyword)

    for association in associations:
        if not G.has_node(association[0]):
            G.add_node(association[0])

        G.add_edge(keyword, association[0])



if __name__ == "__main__":
    input_data_tag = 'korpus-pan'
    number_of_elements = 20

    karabin_associations = sorted_list_with_n_tuples_containing_biggest_values(read_from_json('../results/' + input_data_tag + "_" + 'karabin.json'), number_of_elements)
    kula_associations = sorted_list_with_n_tuples_containing_biggest_values(read_from_json('../results/' + input_data_tag + "_" + 'kula.json'), number_of_elements)
    wojsko_associations = sorted_list_with_n_tuples_containing_biggest_values(read_from_json('../results/' + input_data_tag + "_" + 'wojsko.json'), number_of_elements)
    zolnierz_associations = sorted_list_with_n_tuples_containing_biggest_values(read_from_json('../results/' + input_data_tag + "_" + 'żołnierz.json'), number_of_elements)

    G = nx.Graph()

    add_associations(G, "karabin", karabin_associations)
    add_associations(G, "kula", kula_associations)
    add_associations(G, "wojsko", wojsko_associations)
    add_associations(G, "żołnierz", zolnierz_associations)

    nx.write_gexf(G.to_undirected(), 'graph-' + input_data_tag + '.gexf')


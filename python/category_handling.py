import json
import csv


def read_categories(file_name):
    f = open(file_name)
    js_file = json.load(f)
    f.close()
    return js_file


def load_categories(cat_map_file):
    rows = {}
    with open(cat_map_file, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows[row[0]] = row[1:3]

    return rows

def match_categories(cat_map_file):
    cat_map = load_categories(cat_map_file)


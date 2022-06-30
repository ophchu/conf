from category_handling import read_categories, load_categories
from read_files import read_isracard, write_outputfile, write_transactions


def test_test():
    file_name = "../resources/categories.json"
    cats = read_categories(file_name)
    print(cats)


def test_2():
    t = load_categories("../resources/categories_map.csv")
    print(t)


def test_categories():
    # file_name = "../resources/Export_1_2022_small.xlsx"
    file_name = "../resources/Export_1_2022.xlsx"
    cats = load_categories("../resources/categories_map.csv")
    transactions = read_isracard(file_name, cats)
    write_outputfile(transactions, '../resources/transactions.csv')
    write_transactions(transactions, '../resources/transactions.xlsx')
    print()

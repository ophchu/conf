from read_files import read_isracard


def test_test():
    file_name = "../resources/Export_1_2022_small.xlsx"
    transactions = read_isracard(file_name)
    for tx in transactions:
        print(tx)
    assert len(transactions) == 21

    counts = {}

    for txs in transactions:
        if txs.account not in counts:
            counts[txs.account] = {
                "sum": 0,
                "count": 0
            }
        counts[txs.account]["count"] = counts[txs.account]["count"] + 1
        counts[txs.account]["sum"] = counts[txs.account]["sum"] + txs.amount

    print(counts)


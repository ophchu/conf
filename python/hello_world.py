from python.read_files import read_isracard

filename = "/home/ophchu/MEGA/Bank/תקציב/ישראכרט/Export_1_2022.xlsx"
transactions = read_isracard(filename)

print(transactions[0])


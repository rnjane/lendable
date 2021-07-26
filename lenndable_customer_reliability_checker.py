import csv
from datetime import datetime, timedelta

def reliability_checker(transactions_csv_file_path, n):
    with open(transactions_csv_file_path) as csv_file:
        accounts_dict = {}
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == "customer_id":
                pass
            else:
                if row[0] in accounts_dict:
                    accounts_dict[row[0]].append(datetime.fromisoformat(row[2]).date())
                else:
                    accounts_dict[row[0]] = [datetime.fromisoformat(row[2]).date()]
    calculate_consecutive_days(accounts_dict, n)


def calculate_consecutive_days(accounts_dict, n):
    account_max = {}
    for account, dates in accounts_dict.items():
        dates.sort()
        consecutive_count = 0
        current_max = 0
        for index, date in enumerate(dates):
            if index < len(dates) - 1:
                if date + timedelta(days=1) == dates[index + 1]:
                    consecutive_count += 1
                elif date == dates[index + 1]:
                    pass
                else:
                    if account in account_max:
                        account_max[account] = max(account_max[account], consecutive_count)
                    else:
                        account_max[account] = consecutive_count
                    current_max = max(current_max, consecutive_count)
                    consecutive_count = 0

    max_values = {}
    for account, value in account_max.items():
        if value in max_values:
            max_values[value].append(account)
        else:
            max_values[value] = [account]

    lst = dict(sorted(max_values.items(), key=lambda item: item[0], reverse=True))

    flat_list = []
    for sublist in lst.values():
        sublist.sort()
        for item in sublist:
            flat_list.append(item)
    print(flat_list[:n])


reliability_checker('transaction_data_1.csv', 1)
reliability_checker('transaction_data_2.csv', 2)
reliability_checker('transaction_data_3.csv', 3)
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json

import pandas as pd
from os import listdir


def create_csv_with_json():
    files = listdir()

    list_of_csv = []
    for file in files:
        if file.endswith(".json"):
            with open(file, "r") as file:
                jsfile = json.load(file)
                list_of_csv.append(jsfile)

    csv = pd.DataFrame(list_of_csv)
    print(csv)


if __name__ == '__main__':
    create_csv_with_json()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

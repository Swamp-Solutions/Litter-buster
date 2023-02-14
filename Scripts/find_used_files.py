import os
import re
import pandas as pd

from collections import defaultdict

DATA_PATH = 'C:\\Users\\mcvk\\Downloads\\dataset\\equilized_dataset - 5 plastic 6 paper\\images\\'
CHECK_PATH = 'C:\\Users\\mcvk\\Downloads\\dataset\\validation_dataset\\'


def check_files():
    counter = 0

    for file in os.scandir(DATA_PATH):
        file_name_data = os.path.basename(file)

        for file in os.scandir(f'{CHECK_PATH}\\images\\'):
            file_name_check = os.path.basename(file)
            # file_name_data = re.search("\d+.jpg", file_name_data)
            # file_name_data = file_name_data.group()
            # print(file_name_data)
            # print(file_name_check)
            if file_name_check == file_name_data:
                counter += 1
                os.remove(f'{CHECK_PATH}\\images\\{file_name_check}')
                os.remove(f'{CHECK_PATH}\\labels\\{file_name_check[:-4]}.txt')
                break
    print(f'Files removed: {counter}')


if __name__ == "__main__":
    check_files()

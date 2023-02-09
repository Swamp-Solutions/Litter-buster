import os
import re
import pandas as pd

from collections import defaultdict

DATA_PATH = 'C:\\Users\\mcvk\\Downloads\\dups\\images\\'
CHECK_PATH = 'C:\\Users\\mcvk\\Downloads\\trash\\plastOpol\\images\\images\\'


def check_files():
    counter = 0

    for file in os.scandir(CHECK_PATH):
        file_name_check = os.path.basename(file)

        for file in os.scandir(DATA_PATH):
            file_name_data = os.path.basename(file)
            file_name_data = re.search("\d+.jpg", file_name_data)
            file_name_data = file_name_data.group()
            if file_name_check == file_name_data:
                counter += 1
                os.remove(f'{CHECK_PATH}{file_name_check}')
                break
    print(counter)


if __name__ == "__main__":
    check_files()

import os
import re
import pandas as pd

from collections import defaultdict

PATH = 'C:\\Users\\mcvk\\Downloads\\dups2\\images\\'
print(PATH)


def count_files():

    file_dict = defaultdict(lambda: 0)

    for file in os.scandir(PATH):

        file_name = os.path.basename(file)
        file_name = re.search("\d+.jpg", file_name)
        file_name = file_name.group()
        file_dict[str(file_name)] += 1

    return file_dict


my_dict = count_files()
df = pd.DataFrame(my_dict.items())
duplicates = df.loc[df[1] > 1]
print(duplicates)


if __name__ == "__main__":
    count_files()

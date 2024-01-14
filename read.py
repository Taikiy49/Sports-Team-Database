from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple

def readFile(file: Path) -> List[Tuple[str, str, str]]:
    my_list = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if all(row):  # checks if all elements in the row are non-empty
                my_list.append((row[0], row[1], row[2]))
            else:
                raise ValueError
        my_list.pop(0)  # remove header
        return my_list

def readAllFiles() -> List[SportClub]:
    csv_dir = Path('./')
    csv_files = list(csv_dir.glob('*.csv'))
    #csv_files = ['junesurvey.csv', 'marchsurvey.csv'] #testing purposes
    entire_list = []
    count_dict = {}
    good_files_count = 0
    good_files_line_count = 0
    for file in csv_files:
        try:
            tup_list = readFile(file)
            for tup in tup_list:
                good_files_line_count += 1
                if tup not in count_dict:
                    count_dict[tup] = 1
                else:
                    count_dict[tup] += 1
            good_files_count += 1
        except ValueError:
            with open('error_log.txt', 'a') as file2:
                file2.write(str(file) + '\n')
    with open('report.txt', 'w') as file1:
        file1.write(f'Number of files read: {good_files_count}\n')
        file1.write(f'Number of lines read: {good_files_line_count}\n')
    for i in count_dict.keys():
        obj = SportClub(i[0], i[1], i[2], count_dict[i])
        entire_list.append(obj)
    return entire_list


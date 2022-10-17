import csv
from typing import Any, List

class CSVFileManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def update_tsv_file_line(self, file: List, new_line: str, index: int) -> None:
        file[index] = new_line
        with open(self.file_path, 'w', encoding='utf-8') as opened_file:
            opened_file.writelines(file)
    
    def add_line_to_tsv_file(self, line: str) -> None:
        with open(self.file_path, 'a+', encoding='utf-8') as opened_file:
            opened_file.write(line)

    def read_tsv_file(self) -> List:
        print(f'Lendo arquivo TSV: {self.file_path}')
        result = []
        with open(self.file_path, 'r', encoding='utf-8') as opened_file:
            file_read = csv.reader(opened_file, delimiter='\t')
            for row in file_read:
                result.append(row)
        print('File extracted Data: ', result)
        return result
        
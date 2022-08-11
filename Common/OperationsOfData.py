import os

import pandas

class operations_of_data:
    def __init__(self, file):
        self.file = file

    def to_list(self, **kwargs):
        file_type = os.path.splitext(self.file)[-1][1:]
        if file_type == 'csv':
            return pandas.read_csv(self.file, kwargs).values.tolist()
        elif file_type == 'xlsx':
            return pandas.read_excel(self.file, kwargs).values.tolist()
        elif file_type == 'xls':
            return pandas.read_excel(self.file, kwargs).values.tolist()
        else:
            raise TypeError("An unsupported file type")

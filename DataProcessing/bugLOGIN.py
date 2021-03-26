import xlrd


class ExcelUtil:
    def __init__(self, excel_path, sheet_name):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        # 获取第一行作为key
        self.keys = self.table.row_values(0)  # 行数用下标
        # 获取总行数
        self.rows = self.table.nrows
        # 获取总列数
        self.cols = self.table.ncols
        # Excel数据获取已完成

    def dict_data(self):
        if self.rows <= 1:  # 行数小于等于一行说明没数据或者只有列的说明
            print('数据不足')
        else:
            disc_excel = []
            x = 1
            for i in range(self.rows - 1):
                json = {}

                values_row = self.table.row_values(x)
                for j in range(self.cols):
                    if type(values_row[j]) is float:
                        json[self.keys[j]] = str(int(values_row[j]))  # 账号密码都是纯数字，上面那步会自动改为float,所以这里做数据类型转换处理
                    elif type(values_row[j]) is int:
                        json[self.keys[j]] = str(values_row[j])
                    else:
                        json[self.keys[j]] = values_row[j]
                disc_excel.append(json)
                x += 1
            return disc_excel

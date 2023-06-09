import jsonpath


class GetKeyword:
    @staticmethod
    def get_keyword(source_data, keyword):
        """
        通过关键字获取对应的值,如果有多个值,默认获取第一个,如果没有返回False
        :param source_data: 源数据
        :param keyword: 关键字
        :return: 关键字对应的第一个值/False
        """
        try:
            return jsonpath.jsonpath(source_data, f'$..{keyword}')[0]
        except:
            print(f"{source_data}中,关键字{keyword}不存在")
            return False

    @staticmethod
    def get_keywords(source_data, keyword):
        """
        通过关键字获取对应的所有值,如果不存在,返回False
        :param source_data: 源数据
        :param keyword: 关键字
        :return: list/False
        """
        try:
            return jsonpath.jsonpath(source_data, f'$..{keyword}')
        except:
            print(f"{source_data}中,关键字{keyword}不存在")
            return False

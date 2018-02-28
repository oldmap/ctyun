import MySQLdb


ASSET_DB = {
    'host': '10.35.129.82',
    'port': 3306,
    'user': 'query',
    'passwd': 'Query@2017',
    'db': 'bdmp',
    'charset': 'utf8'
}


class Asset_info():
    """
        从资产管理数据中以IP为索引，查询除所有相关信息，并返回字典格式数据
    """
    def __init__(self, *args, **kwargs):
        self.mysql = self.__connect(**ASSET_DB)
        self.dict_table, self.dict_table_r = self.__get_dict_table()
        self.columns = self.__get_columns()
        # 接受所有字典格式查询条件
        self.kwargs = kwargs
        print(self.kwargs)

    def __connect(self, **kwargs):
        try:
            mysql = MySQLdb.connect(**kwargs)
            return mysql
        except Exception as e:
            print('数据库链接失败：%s' % e.__str__())

    def __get_dict_table(self):
        # 正向字典 'bb9c707864bd4a7cad7456b01a07bb7d': 'DCS7200Z'
        dict_table = {}
        # 反向字典 'DCS7200Z'：'bb9c707864bd4a7cad7456b01a07bb7d'
        dict_table_r = {}
        # 将字典表所有数据输出查询出来，拼接python字典格式
        c = self.mysql.cursor()
        sql_query = "SELECT code,name FROM mp_conf_dictitem;"
        c.execute(sql_query)
        value = c.fetchall()
        for v in value:
            dict_table[v[0]] = v[1]
            dict_table_r[v[1]] = v[0]
        return dict_table, dict_table_r

    def __get_columns(self):
        columns = []
        # 将字典表所有数据输出查询出来，拼接python字典格式
        c = self.mysql.cursor()
        sql_query = "desc mp_host_machine;"
        c.execute(sql_query)
        value = c.fetchall()
        for v in value:
            columns.append(v[0])
        return columns

    def info(self):
        info_list = []
        # 可以多条件查询资产信息， 按时不支持 yinstructs 列
        index_list = []
        mapd_keys = ['machinetype', 'clusterinfo', 'grouptype', 'platformtype', 'position']
        for key in self.kwargs:
            if key in mapd_keys:
                index_str = " %s like '%s' " % (key, self.dict_table_r.get(self.kwargs.get(key)))
            else:
                index_str = " %s like '%s' " % (key, self.kwargs.get(key))
            index_list.append(index_str)
        if index_list:
            all_index_str = ('and').join(index_list)
            """通过ip查询资产管理数据库，放回单条数据"""
            # sql_query = "SELECT *, NULL AS checkTime FROM mp_host_machine WHERE %s;" % all_index_str
            sql_query = "SELECT * FROM mp_host_machine WHERE %s;" % all_index_str
        else:
            # sql_query = "SELECT *, NULL AS checkTime FROM mp_host_machine;"
            sql_query = "SELECT * FROM mp_host_machine;"
        print(sql_query)

        c = self.mysql.cursor()
        c.execute(sql_query)
        result_list = c.fetchall()
        for result in result_list:
            if result:
                # 虚拟机和物理机不再一个表里，字段也不相同，虚拟机的暂时忽略
                data = dict(map(lambda x, y: [x, y], self.columns, result))

                # 偷懒，删除checkTime字段，防止 json to string时 出错
                data['checkTime'] = ''

                # 要关联的查询
                mapd_keys = ['machinetype', 'clusterinfo', 'grouptype', 'platformtype', 'position']
                for key in mapd_keys:
                    # print(key)
                    # print(data[key])
                    data[key] = self.dict_table.get(data[key])
                tmp = []
                if data['yinstructs']:    # yinstructs可能为空
                    yinstructs_list = data['yinstructs'].split('、')
                    for item in yinstructs_list:
                        tmp.append(self.dict_table[item])
                    data['yinstructs'] = ('、').join(tmp)

                info_list.append(data)
            else:
                info_list.append({})
        return info_list


# if __name__ == '__main__':
    # 可以多条件查询资产信息
    # asset = Asset_info(ip='10.0.171.27', machinetype='DCS7200Z')
    # print(asset.dict_table)
    # print(asset.columns)
    # asset = Asset_info(ip='10.0.171.27', machinetype='DCS7200Z')

    # asset = Asset_info(vlan='218', machinetype='DCS7200Z')
    # asset_list = asset.info()
    # print(len(asset_list))
    # print(asset_list)




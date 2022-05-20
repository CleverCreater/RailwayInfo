class ModelMetaClass(type):
    def __new__(mcs, name, bases, attrs):
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, tuple):
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        # 将attrs中的属性转化为以下形式
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name

        return type.__new__(mcs, name, bases, attrs)


class Model(object, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            # 获取所有字段名
            fields.append(v[0])
            # 获取字段名对应的值
            args.append(getattr(self, k, None))

        # 给args中的值，如果不是数字，则需要加上引号（SQL中需要加引号，这里加单引号）
        args_temp = list()
        for temp in args:
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)

        # 组合SQL
        sql = """insert into %s (%s) values (%s)""" % (self.__table__, ','.join(fields), ','.join(args_temp))
        return sql


class NewTable:
    def __init__(self, mappings: dict, table: str):
        self.mappings = mappings
        self.table = table

    def __str__(self):
        title = ''  # 数据库表头
        for k, v in self.mappings.items():
            title += (v[0] + ' ' + v[1] + ',')
        return 'create table ' + self.table + '(' + title[0: -1] + ')'

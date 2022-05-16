"""
Train Number
匹配车次
"""
import re


# 高铁
class HighSpeed:
    def __init__(self, get):
        self.out = get

    def __repr__(self):
        return ()


# 动车
class Bullet:
    def __init__(self, get):
        self.out = get


# 城际
class InterCity:
    def __init__(self, get):
        self.out = get


# 直达
class NonStop:
    def __init__(self, get):
        self.out = get


# 特快
class Express:
    def __init__(self, get):
        self.out = get


# 快速
class Fast:
    def __init__(self):
        pass


# 慢车
class Slow:
    def __init__(self):
        pass


# 临时
class Temporary:
    def __init__(self, get):
        self.out = get


# 旅游
class Tour:
    def __init__(self, get):
        self.out = get


template = {
    'G/*\\d{1,3}': HighSpeed,
    'D/*\\d{1,3}': Bullet,
    'C/*\\d{1,3}': InterCity,
    'Z/*\\d{1,3}': NonStop,
    'T/*\\d{1,3}': Express,
    'K/*\\d{1,3}': Fast,
    '\\d{1,4}': Slow,
    'L/*\\d{1,3}': Temporary,
    'A/*\\d{1,3}': Temporary,
    'Y/*\\d{1,3}': Tour,
}


class Main:
    def __init__(self, get: str):
        out = False
        if re.match('[GDCZTKLYS]', get):
            for k, v in template.items():
                if re.match(k, get):
                    out = v(get[1:].split('/')[-1]).out
        self.out = out

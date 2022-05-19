"""
Train Number
匹配车次
"""
import re


class NumberError(Exception):
    def __init__(self, num):
        print('Number ' + num + " isn't correct")


class Train:
    def __init__(self, get):
        try:
            self.out = int(get)
        except ValueError:
            raise NumberError(get)
        self.form = {}
        self.name = 'Train'

    def __str__(self):
        for k, v in self.form.items():
            if k:
                return self.name + v
        else:
            return 'ERROR'


# 高铁
class HighSpeed(Train):
    def __init__(self, get):
        super(HighSpeed, self).__init__(get)
        self.name = '高铁'
        self.form = {
            1001 <= self.out <= 5998: '跨局',
            6001 <= self.out <= 9998: '管内',
        }


# 动车
class Bullet(Train):
    def __init__(self, get):
        super(Bullet, self).__init__(get)
        self.name = '动车'
        self.form = {
            1 <= self.out <= 3998: '跨局',
            4501 <= self.out <= 4580: '北京',
            5001 <= self.out <= 5050: '沈阳',
            5051 <= self.out <= 5100: '西安',
            5401 <= self.out <= 5700: '上海',
            6001 <= self.out <= 6500: '济南',
            7001 <= self.out <= 7300: '广铁',
            8201 <= self.out <= 8400: '南宁'
        }


# 城际
class InterCity(Train):
    def __init__(self, get):
        super(InterCity, self).__init__(get)
        self.name = '城际'
        self.form = {
            1001 <= self.out <= 5998: '跨局',
            6001 <= self.out <= 9998: '管内',
        }


# 直达
class NonStop(Train):
    def __init__(self, get):
        super(NonStop, self).__init__(get)
        self.name = '直达'
        self.form = {
            1 <= self.out <= 1998: ''
        }


# 特快
class Express(Train):
    def __init__(self, get):
        super().__init__(get)
        self.form = {
            1 <= self.out <= 5000: '跨局',
            5001 <= self.out <= 5300: '哈尔滨',
            5301 <= self.out <= 5600: '沈阳',
            5601 <= self.out <= 6000: '北京',
            6001 <= self.out <= 6300: '太原',
            6301 <= self.out <= 6400: '呼和浩特',
            6401 <= self.out <= 6700: '郑州',
            6701 <= self.out <= 7000: '武汉',
            7001 <= self.out <= 7300: '西安',
            7301 <= self.out <= 7600: '济南',
            7601 <= self.out <= 8000: '上海',
            8001 <= self.out <= 8300: '南昌',
            8301 <= self.out <= 8700: '广铁',
            8701 <= self.out <= 8800: '南宁',
            8801 <= self.out <= 9000: '成都',
            9001 <= self.out <= 9200: '昆明',
            9201 <= self.out <= 9400: '兰州',
            9401 <= self.out <= 9600: '乌鲁木齐',
            9601 <= self.out <= 9800: '青藏',
            9801 <= self.out <= 9998: '增补',
        }
        self.name = '特快'


# 快速
class Fast(Train):
    def __init__(self, get):
        super(Fast, self).__init__(get)
        self.form = {
            1 <= self.out <= 6998: '跨局',
            7001 <= self.out <= 7300: '哈尔滨',
            7301 <= self.out <= 7600: '沈阳',
            7701 <= self.out <= 7800: '北京',
            7801 <= self.out <= 7900: '太原',
            7901 <= self.out <= 7950: '呼和浩特',
            7951 <= self.out <= 8050: '郑州',
            8051 <= self.out <= 8150: '武汉',
            8151 <= self.out <= 8250: '西安',
            8251 <= self.out <= 8350: '济南',
            8351 <= self.out <= 8700: '上海',
            8701 <= self.out <= 9000: '南昌',
            9001 <= self.out <= 9300: '广铁',
            9301 <= self.out <= 9350: '南宁',
            9351 <= self.out <= 9600: '成都',
            9601 <= self.out <= 9660: '昆明',
            9661 <= self.out <= 9740: '兰州',
            9741 <= self.out <= 9800: '乌鲁木齐',
            9801 <= self.out <= 9850: '青藏',
        }
        self.name = '快速'


# 慢车
class Slow(Train):
    def __init__(self, get):
        super(Slow, self).__init__(get)
        self.form = {
            # 普快
            1001 <= self.out <= 4000: '普快跨局',
            4001 <= self.out <= 4200: '普快哈尔滨',
            4201 <= self.out <= 4400: '普快沈阳',
            4401 <= self.out <= 4600: '普快北京',
            4601 <= self.out <= 4650: '普快太原',
            4651 <= self.out <= 4700: '普快呼和浩特',
            4701 <= self.out <= 4800: '普快郑州',
            4801 <= self.out <= 4900: '普快武汉',
            4901 <= self.out <= 5000: '普快西安',
            5001 <= self.out <= 5050: '普快济南',
            5051 <= self.out <= 5200: '普快上海',
            5201 <= self.out <= 5300: '普快南昌',
            5301 <= self.out <= 5500: '普快广铁',
            5501 <= self.out <= 5550: '普快南宁',
            5551 <= self.out <= 5650: '普快成都',
            5651 <= self.out <= 5700: '普快昆明',
            5701 <= self.out <= 5800: '普快兰州',
            5801 <= self.out <= 5900: '普快乌鲁木齐',
            5901 <= self.out <= 5998: '普快青藏',
            # 普慢
            6001 <= self.out <= 6200: '普慢跨局',
            6201 <= self.out <= 6300: '普慢哈尔滨',
            6301 <= self.out <= 6400: '普慢沈阳',
            6401 <= self.out <= 6500: '普慢北京',
            6801 <= self.out <= 6850: '普慢太原',
            6851 <= self.out <= 6900: '普慢呼和浩特',
            6901 <= self.out <= 6950: '普慢郑州',
            6951 <= self.out <= 7000: '普慢武汉',
            7001 <= self.out <= 7050: '普慢西安',
            7051 <= self.out <= 7100: '普慢济南',
            7101 <= self.out <= 7200: '普慢上海',
            7201 <= self.out <= 7250: '普慢南昌',
            7251 <= self.out <= 7300: '普慢广铁',
            7301 <= self.out <= 7350: '普慢南宁',
            7351 <= self.out <= 7450: '普慢成都',
            7451 <= self.out <= 7500: '普慢昆明',
            7501 <= self.out <= 7550: '普慢兰州',
            7551 <= self.out <= 7580: '普慢乌鲁木齐',
            7581 <= self.out <= 7598: '普慢青藏',
            # 通勤
            7601 <= self.out <= 7798: '通勤哈尔滨',
            7801 <= self.out <= 7998: '通勤沈阳',
            8001 <= self.out <= 8150: '通勤北京',
            8151 <= self.out <= 8198: '通勤太原',
            8201 <= self.out <= 8250: '通勤呼和浩特',
            8251 <= self.out <= 8298: '通勤郑州',
            8301 <= self.out <= 8350: '通勤武汉',
            8351 <= self.out <= 8398: '通勤西安',
            8401 <= self.out <= 8450: '通勤济南',
            8451 <= self.out <= 8550: '通勤上海',
            8551 <= self.out <= 8598: '通勤南昌',
            8601 <= self.out <= 8698: '通勤广铁',
            8701 <= self.out <= 8750: '通勤南宁',
            8751 <= self.out <= 8850: '通勤成都',
            8851 <= self.out <= 8898: '通勤昆明',
            8901 <= self.out <= 8950: '通勤兰州',
            8951 <= self.out <= 8980: '通勤乌鲁木齐',
            8981 <= self.out <= 8998: '通勤青藏',
        }
        self.name = '慢速'


# 临时
class Temporary(Train):
    def __init__(self, get):
        super(Temporary, self).__init__(get)
        self.form = {
            1 <= self.out <= 6998: '跨局',
            7001 <= self.out <= 7300: '哈尔滨',
            7301 <= self.out <= 7600: '沈阳',
            7701 <= self.out <= 7800: '北京',
            7801 <= self.out <= 7900: '太原',
            7901 <= self.out <= 7950: '呼和浩特',
            7951 <= self.out <= 8050: '郑州',
            8051 <= self.out <= 8150: '武汉',
            8151 <= self.out <= 8250: '西安',
            8251 <= self.out <= 8350: '济南',
            8351 <= self.out <= 8700: '上海',
            8701 <= self.out <= 9000: '南昌',
            9001 <= self.out <= 9300: '广铁',
            9301 <= self.out <= 9350: '南宁',
            9351 <= self.out <= 9600: '成都',
            9601 <= self.out <= 9660: '昆明',
            9661 <= self.out <= 9740: '兰州',
            9741 <= self.out <= 9800: '乌鲁木齐',
            9801 <= self.out <= 9850: '青藏',
        }
        self.name = '临时'


# 旅游
class Tour(Train):
    def __init__(self, get):
        super(Tour, self).__init__(get)
        self.form = {
            1 <= self.out <= 498: '跨局',
            501 <= self.out <= 530: '哈尔滨',
            531 <= self.out <= 560: '沈阳',
            561 <= self.out <= 600: '北京',
            601 <= self.out <= 630: '太原',
            631 <= self.out <= 640: '呼和浩特',
            641 <= self.out <= 670: '郑州',
            671 <= self.out <= 700: '武汉',
            701 <= self.out <= 730: '西安',
            731 <= self.out <= 760: '济南',
            761 <= self.out <= 800: '上海',
            801 <= self.out <= 830: '南昌',
            831 <= self.out <= 870: '广铁',
            871 <= self.out <= 880: '南宁',
            881 <= self.out <= 900: '成都',
            901 <= self.out <= 920: '昆明',
            921 <= self.out <= 940: '兰州',
            941 <= self.out <= 960: '乌鲁木齐',
            961 <= self.out <= 980: '青藏',
        }
        self.name = '旅游'


template = {
    'G/*\\d{1,4}': HighSpeed,
    'D/*\\d{1,4}': Bullet,
    'C/*\\d{1,4}': InterCity,
    'Z/*\\d{1,4}': NonStop,
    'T/*\\d{1,4}': Express,
    'K/*\\d{1,4}': Fast,
    '\\d{1,4}': Slow,
    'L/*\\d{1,3}': Temporary,
    'A/*\\d{1,3}': Temporary,
    'Y/*\\d{1,3}': Tour,
}


class Main:
    def __init__(self, get: str):
        out = 'NULL'
        if type(get) != str:
            out = 'Input Problem'
        elif re.match('[GDCZTKLYS\\d{4}]', get):
            for k, v in template.items():
                if re.match(k, get):
                    if re.match('\\d{4}', get):
                        get = ' ' + get
                    try:
                        out = v(get[1:].split('/')[-1]).__str__()
                    except NumberError:
                        out = 'Wrong'
        else:
            out = 'Not Find'
        self.out = out

    def __str__(self):
        return self.out

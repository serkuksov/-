one_to_nineteen = (u'ноль',
                   u'один', u'два', u'три', u'четыре', u'пять', u'шесть', u'семь', u'восемь', u'девять',
                   u'десять', u'одиннадцать', u'двенадцать', u'тринадцать', u'четырнадцать', u'пятнадцать',
                   u'шестнадцать', u'семнадцать', u'восемнадцать', u'девятнадцать')

one_to_nineteen_woman = (u'ноль',
                   u'одна', u'две', u'три', u'четыре', u'пять', u'шесть', u'семь', u'восемь', u'девять',
                   u'десять', u'одиннадцать', u'двенадцать', u'тринадцать', u'четырнадцать', u'пятнадцать',
                   u'шестнадцать', u'семнадцать', u'восемнадцать', u'девятнадцать')

decs = ('', u'десять', u'двадцать', u'тридцать', u'сорок',
        u'пятьдесят', u'шестьдесят', u'семьдесят', u'восемьдесят', u'девяносто')

hundreds = ('', u'сто', u'двести', u'триста', u'четыреста',
            u'пятьсот', u'шестьсот', u'семьсот', u'восемьсот', u'девятьсот')

thousands = ('', u'одна тысяча', u'две тысячи', u'три тысячи', u'четыре тысячи')


def _one_convert(integer):
    return one_to_nineteen[integer]


def _two_convert(integer, string):
    if integer in range(20):
        result = one_to_nineteen[integer]
    else:
        result = decs[int(string[0])]
        if string[1] != '0':
            result = u'%s %s' % (result, one_to_nineteen[int(string[1])])
    return result


def _one_convert_woman(integer):
    return one_to_nineteen_woman[integer]


def _two_convert_woman(integer, string):
    if integer in range(20):
        result = one_to_nineteen_woman[integer]
    else:
        result = decs[int(string[0])]
        if string[1] != '0':
            result = u'%s %s' % (result, one_to_nineteen_woman[int(string[1])])
    return result


def convert(string):
    length = len(string)
    integer = int(string)
    if length == 1:
        result = _one_convert(integer)
    elif length == 2:
        result = _two_convert(integer, string)
    elif length == 3:
        result = hundreds[int(string[0])]
        tail = string[-2:]
        if tail != '00':
            result = u'%s %s' % (result, convert(tail))
    elif length in range(4, 7):
        tail = convert(string[-3:])
        str_head = string[:-3]
        int_head = int(str_head)
        if int_head % 10 in range(1, 5) and int_head > 19:
            head = convert(str_head[:-1] + '0') + ' ' + thousands[int_head % 10]
            # head = thousands[int_head % 10]
        elif int_head in range(1, 5):
            head = thousands[int_head]
        else:
            head = u'%s тысяч' % (convert(str_head))
        result = u'%s %s' % (head, tail)
    else:
        result = ''
    return result.strip()


def convert_woman(string):
    length = len(string)
    integer = int(string)
    if length == 1:
        result = _one_convert_woman(integer)
    elif length == 2:
        result = _two_convert_woman(integer, string)
    elif length == 3:
        result = hundreds[int(string[0])]
        tail = string[-2:]
        if tail != '00':
            result = u'%s %s' % (result, convert(tail))
    elif length in range(4, 7):
        tail = convert(string[-3:])
        str_head = string[:-3]
        int_head = int(str_head)
        if int_head % 10 in range(1, 5) and int_head > 19:
            head = convert(str_head[:-1] + '0') + ' ' + thousands[int_head % 10]
            # head = thousands[int_head % 10]
        elif int_head in range(1, 5):
            head = thousands[int_head]
        else:
            head = u'%s тысяч' % (convert(str_head))
        result = u'%s %s' % (head, tail)
    else:
        result = ''
    return result.strip()


def convert_price(price):
        rubles = int(price // 1)
        kopecks = round(price % 1 * 100)
        # print(kopecks)
        if 1 < kopecks % 10 < 5:
                kopecks_pr = 'копейки'
        elif kopecks % 10 == 1:
                kopecks_pr = 'копейка'
        else:
                kopecks_pr = 'копеек'
        if 1 < rubles % 10 < 5:
                rubles_pr = 'белорусских рубля'
        elif rubles % 10 == 1:
                rubles_pr = 'белорусский рубль'
        else:
                rubles_pr = 'белорусских рублей'
        rubles = convert(str(rubles))
        kopecks = convert_woman(str(kopecks))
        prize_str = f'{rubles} {rubles_pr} {kopecks} {kopecks_pr}'
        return prize_str


if __name__ == '__main__':
    import random

    for i in range(2000, 10000, random.randint(1, 300)):
        print(convert(str(i)))

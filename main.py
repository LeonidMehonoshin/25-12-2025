import random

def test1(_list):
    def max_index(_list, num=0):
        _max = 0
        for i in range(len(_list)-num):
            if _list[_max] < _list[i]: _max = i
        return _max
    _1_bigger_2 = 0
    for i in range(len(_list)-1):
        if _list[i] < _list[i+1]: _1_bigger_2 += 1
    return {
        'Test': 1,
        'Список': _list,
        'Максимальный': max_index(_list),
        'Второй максимальный': max_index(_list, 1),
        'Третий максимальный': max_index(_list, 2),
        'Первый больше второго': _1_bigger_2
    }

def test2(_list, _list2):
    result = _list.copy()
    for num in _list2:
        found = False
        for i in range(len(result)):
            if result[i] > num:
                result.insert(i, num)
                found = True
                break
        if not found: result.append(num)
    return {
        'Test': 2,
        'Список 1': _list,
        'Список 2': _list2,
        'Слияние двух списков': result
    }

def test3(_list):
    result = []
    for i in range(len(_list)-1):
        if ((_list[i] % 2 == 0 and _list[i+1] % 2 == 0) or
            (_list[i] % 2 != 0 and _list[i+1] % 2 != 0)):
                result.append([_list[i], _list[i+1]])

    top3 = [[], [], []]; current = [_list[0]]
    for num in _list[1:]:
        if num > current[-1]: current.append(num)
        else:
            for i in range(3):
                if len(current) > len(top3[i]):
                    top3[i] = current[:]; break
            current = [num]

    for i in range(3):
        if len(current) > len(top3[i]): top3[i] = current; break

    return {
        'Test': 3,
        'Список': _list,
        'Пары сумма, которых нечетна': result,
        'Количество уникальных элементов': len(set(_list)),
        '3 самые длинные, отсортированные последовательности': top3
    }

results = {
    'test1': test1([1,4,5,4,3,5,2,4,2,4,3]),
    'test2': test2([i for i in range(15)],
            [i for i in range(3, 27, 2)]),
    'test3': test3([random.randint(0,100) for i in range(30)])
}
for test_name in results:
    result = results[test_name]
    try:
        for key, value in result.items():
            print(f"'{key}': {value},")
    except AttributeError: print(result)
    print()

def sl():
    _set = {}
    s = input()
    while s != '':
        _s = s.split()
        _set[_s[0]+' '+_s[1]] = int(_s[2])
        s = input()
    return _set


inf = dict()
mat = dict()
phys = dict()

print('Введите количество олимпиад')
count = int(input())
_list_dict = [0]*count
for i in range(0, count):
    _list_dict[i] = sl()

for _set in _list_dict:
    print(_set)

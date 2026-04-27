# import MOKO
#
# #Region Временные данные
# #description: Дата;Время
# #hash Дата и время: 12.08.2022;16:41
#
# hash = "Дата и время"
# MOKO.Program("tree", "set", "select = " + hash)
#
# MOKO.Program("tree", "set", "chosen = passed")
#
# MOKO.EndScript()

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    else:
        i = i+1
else:
    print(X, 'not found')
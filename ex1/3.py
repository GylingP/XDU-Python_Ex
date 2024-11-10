import random
lst = [random.randint(0, 100) for i in range(20)]
ascLst = sorted(lst[:10])
descLst= sorted(lst[10:], reverse=True)
ascLst.extend(descLst)
print(ascLst)
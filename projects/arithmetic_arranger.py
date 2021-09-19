import re

def arithmetic_arranger(problems):
    firstnumslst = list()
    firstnums = list()
    secondnumslst = list()
    secondnums = list()
    sum = 0
    for problem in problems:
        firstnumslst = re.findall('^[0-9]*\S', problem)
        secondnumslst = re.findall('[\+\-\*\/] ([0-9]*)', problem)
        for i in firstnumslst:
            firstnums.append(i)
        for i in secondnumslst:
            secondnums.append(i)
    return firstnums, secondnums

print(arithmetic_arranger(['78 + 90', '192 + 39']))


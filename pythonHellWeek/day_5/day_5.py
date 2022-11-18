from typing import List


def range_float(start: float, end: float, step: float=None) -> List[float]:
    list = []
    if step is None:
        if start > 0 and end > 0:
            while start < end - .1:
                for start in list:
                    if start in list:
                        start += .1
                else:
                    list.append(round(start, 1))
        else:
            while start > end + .1:
                for start in list:
                    if start in list:
                        start -= .1
                else:
                    list.append(round(start, 1))
    else:
        if start > 0 and end > 0:
            while start < end - step:
                for start in list:
                    if start in list:
                        start += step
                else:
                    list.append(round(start, 1))
        else:
            while start > end + step:
                for start in list:
                    if start in list:
                        start -= step
                else:
                    list.append(round(start, 1))
    return list


print([number for number in range_float(1.0, 2.0)])
print([number for number in range_float(-1.0, -2.0)])

print([number for number in range_float(1.0, 2.0, .3)])
print([number for number in range_float(-1.0, -2.0, .3)])


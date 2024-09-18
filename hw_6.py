def binary_search(array, target):
    first = 0
    last = len(array) - 1
    result_ok = False
    pos = -1

    while first <= last and not result_ok:
      middle = (first + last) // 2
      if array[middle] == target:
        result_ok = True
        pos = middle
      elif array[middle] < target:
        first = middle + 1
      else:
        last = middle - 1

    if result_ok:
      print("Элемент:", target, "Hайден на позиции:", pos)
    else:
      print("Элемент не найден")
    return pos

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
target = 15
binary_search(array, target)
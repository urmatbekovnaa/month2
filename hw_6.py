def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


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
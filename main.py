lst_array = [int(x) for x in input("Введите последовательность чисел через пробел: ").split()]
number = int(input("Введите любое число: "))
def qsort(lst_array, left, right):
    middle = (left + right) // 2
    p = lst_array[middle]
    i, j = left, right

    while i <= j:
        while lst_array[i] < p:
            i += 1
        while lst_array[j] > p:
            j -= 1
        if i <= j:
            lst_array[i], lst_array[j] = lst_array[j], lst_array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(lst_array, left, j)
    if right > i:
        qsort(lst_array, i, right)
    return lst_array

def my_sort(lst_array):
    return qsort(lst_array, 0, len(lst_array)-1)
print(my_sort(lst_array))

sort_array = my_sort(lst_array)
def binary_search(sort_array, number, left, right):
    if left < 0 or right > len(sort_array)-1:
        return "Условие не выполнено"
    if left > right:  # если левая граница превысила правую,
        return "Условие не выполнено"  # значит элемент отсутствует
    middle_index = (right + left) // 2  # находим середину

    value = sort_array[middle_index]
    if middle_index+1 > len(sort_array)-1:
        next_middle_index = middle_index
    else:
        next_middle_index = middle_index+1
    next_value = sort_array[next_middle_index]

    if value == number:  # если элемент в середине,
        return middle_index  # возвращаем этот индекс
    elif number > value:
        if number <= next_value:
            return middle_index
        else:
            return binary_search(sort_array, number, middle_index+1, right)
    else:
        return binary_search(sort_array, number, left, middle_index-1)
print(binary_search(sort_array, number, 0, len(sort_array)-1))
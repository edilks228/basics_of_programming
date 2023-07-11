def natural_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделение массива на отсортированные подпоследовательности
    sequences = []
    start = 0
    while start < len(arr):
        end = start + 1
        while end < len(arr) and arr[end] >= arr[end - 1]:
            end += 1
        sequences.append(arr[start:end])
        start = end

    # Слияние подпоследовательностей
    while len(sequences) > 1:
        merged_sequences = []
        i = 0
        while i < len(sequences) - 1:
            merged = merge(sequences[i], sequences[i + 1])
            merged_sequences.append(merged)
            i += 2

        # Обработка нечетной последовательности
        if i == len(sequences) - 1:
            merged_sequences.append(sequences[i])

        sequences = merged_sequences

    return sequences[0]


def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Добавление оставшихся элементов
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# Пример использования
arr = [7, 9, 13, 1, 8, 4, 10, 11, 5, 3, 6, 2]
sorted_arr = natural_merge_sort(arr)
print(sorted_arr)
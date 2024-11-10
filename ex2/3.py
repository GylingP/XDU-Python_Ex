def my_sorted(iterable, key=None, reverse=False):
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if key:
                if key(left[i]) < key(right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            else:
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
        result += left[i:]
        result += right[j:]
        return result

    def merge_sort(items):
        if len(items) <= 1:
            return items
        middle = len(items) 
        left = items[:middle]
        right = items[middle:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)

    sorted_list = merge_sort(iterable)

    if reverse:
        sorted_list.reverse()

    return sorted_list

if __name__=="__main__" :
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_numbers = my_sorted(numbers)
    print(sorted_numbers) 

    words = ["hello", "world", "python", "is", "awesome"]
    sorted_words = my_sorted(words, key=len, reverse=True)
    print(sorted_words) 
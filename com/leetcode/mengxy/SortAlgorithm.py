from typing import List


#这都能想好久，也是醉了
#快排在原数组操作即可
def quick_sort(array : List[int], start :int, end :int):
    if end - start < 1:
        return

    mid = _sort_quick(array, start, end)
    quick_sort(array, start, mid-1)
    quick_sort(array, mid+1, end)

#value设为左边，就从右边开始遍历，while判断与value大小时要加入start<end的判断
def _sort_quick(array: List[int], start: int, end: int):
    value = array[start]
    start_index = start
    while start < end:
        while array[end] > value and start < end:
            end -= 1
        while array[start] <= value and start < end:
            start += 1
        swap(array, start, end)
    swap(array, end, start_index)
    return end


def swap(array: List[int], i: int, j: int):
    array[i], array[j] = array[j], array[i]


def merge_sort(array: List[int]) -> List[int]:
    if len(array) < 2:
        return array
    mid = int(len(array) / 2)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return _sort_merge(left, right)


def _sort_merge(left: List[int], right: List[int]) -> List[int]:
    tmp = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            tmp.append(left[0])
            left = left[1:]
        else:
            tmp.append(right[0])
            right = right[1:]
    return tmp + left + right


def bubble_sort(array: List[int]):
    end = int(len(array) / 2) - 1
    for i in range(end, -1, -1):
        _sort_bubble(array, i, len(array))
    swap(array, 0, len(array)-1)
    for i in range(len(array)-2, -1, -1):
        _sort_bubble(array, 0, i)
        swap(array, 0, i)


def _sort_bubble(array: List[int], k: int, end: int):
    length = len(array[:end])
    value = array[k]
    m = 2 * k + 1
    while m < length:
        if m + 1 < length and array[m] > array[m+1]:
            m = m + 1
        if array[m] < value:
            array[k] = array[m]
            k = m
            m = 2 * k + 1
        else:
            break
    array[k] = value



def quick_sort2(nums, begin, end):

    def sort_quick(nums, i, j):
        key_value = nums[begin]
        tmp = i
        while i < j:
            while i < j and nums[j] > key_value:
                j -= 1
            while i < j and nums[i] <= key_value:
                i += 1
            swap(nums, i, j)
        swap(nums, tmp, i)
        return i

    if end - begin >= 1:
        mid = sort_quick(nums, begin, end)
        quick_sort2(nums, begin, mid-1)
        quick_sort2(nums, mid+1, end)


if __name__ == '__main__':
    a = [4, 1, 5, 6, 3, 1]
    b = [8, 1, 3, 3, 45, 2, 5, 1, 9, 2, 6, 7]
    s = _sort_merge([1,2,3],[2,3,4])
    bubble_sort(b)
    quick_sort2(a, 0, 5)
    print(a)




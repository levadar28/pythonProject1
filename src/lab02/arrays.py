def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError("Список не может быть пустым")
    else:
        return min(nums), max(nums)


print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([-5, -2, -9]))


# def unique_sorted(nums: list[float | int]) -> list[float | int]:
#    return sorted(set(nums))
# print(sorted(set([3, 1, 2, 1, 3])))
# print(sorted(set([])))
# print(sorted(set([-1, -1, 0, 2, 2])))
# print(sorted(set([1.0, 1, 2.5, 2.5, 0])))


# def flatten(mat: list[list | tuple]) -> list:
#    result = []
#    for obj in mat:
#        if not isinstance(obj, (list, tuple)):
#            raise TypeError(f"Элемент {obj} не является списком или кортежем")
#        else:
#            for item in obj:
#               result.append(item)
#   return result
# print(flatten([[1, 2], [3, 4]]))
# print(flatten([[1], [], [2, 3]]))
# print(flatten([[1, 2], 'ab']))
# print(flatten([1, 2],(3, 4, 5)))

# 9) Соедините два списка и отсортируйте их. Затем удалите повторяющиеся элементы.


list1 = [1, 2, 33, 4, 5]
list2 = [35, 4, 2, 3, 11]

combined_list = list1 + list2

final_list = list(set(combined_list))

sorted_list = sorted(final_list)

print(sorted_list)

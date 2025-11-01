nums = [-5, 3, 7, 19, 23, 45, 63, 67, 103]
# def search(find_num,列表):
#     mid_val = 找到列表的中间值
#     if find_num > mid_val:
#         # 接下来应该查找的是列表的右半部分
#         新列表 = 切出列表的右半部分
#         search(find_num,新列表)
#     elif find_num < mid_val:
#         # 接下来应该查找的是列表的左半部分
#         新列表 = 切出列表的左半部分
#         search(find_num, 新列表)
#     else:
#         print('find it')
def search(find_num,nums_list):
    mid_index = len(nums_list) // 2
    mid_val=nums_list[mid_index]
    if mid_val < find_num:
        search(find_num,nums_list[mid_index+1:])
    elif mid_val > find_num:
        search(find_num,nums_list[:mid_index])
    else:
        print(find_num)


search(19,nums)
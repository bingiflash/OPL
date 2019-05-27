test_string = "(+ (* 3 5) (* 3 4))"
test_string1 = "(+ 1 (+ 1 (+ 1 1)))"
test_string2 = "(* 3 5)"

# def temp_func(string):
#     elements = []
#     paran_count = 0
#     start_index = 1
#     # stop_index = 0
#     for i, char in enumerate(string):
#         if char is ' ':
#             continue
#         if paran_count == 1:
#             elements.append(string[start_index:i+1])
#             start_index = i+1
#         if char is '(':
#             paran_count += 1
#         if char is ')':
#             paran_count -= 1
#     print(elements)

def temp_func(string):
    elements = []
    paran_count = 0
    start_index = 1
    # stop_index = 0
    for i, item in enumerate(string.split(' ')):
        if paran_count == 1:
            elements.append(string[start_index:i+1])
            start_index = i+1
        if item.count('(') > 0:
            paran_count += 1
        if item.count(')') < 0:
            paran_count -= 1
    print(elements)

temp_func(test_string)
temp_func(test_string1)
temp_func(test_string2)

# class Node:
#     def __init__(self, obj):
#         self.obj = obj
#     def __str__(self):
#         return str(self.obj)

# class se:
#     def __init__(self, string, is_next_small_se):
#         temp_storage = string.split(' ')
#         temp_paran_count = 0
#         temp_i = None
#         self.operator = Node(temp_storage[0][1])
#         del temp_storage[0]
#         if is_next_small_se is False:
#             self.param1 = Node(temp_storage[0])
#             temp_storage = temp_storage[1:].strip()
#             x = temp_storage.split(' ')
#             if x[0].count('(') > 0:
#                 self.param2 = se()

#         else:
#             temp_storage = ' '.join(temp_storage)
#             temp_storage = temp_storage[:-1]
#             for i, char in enumerate(temp_storage):
#                 if char is '(':
#                     temp_paran_count += 1
#                 if char is ')':
#                     temp_paran_count -= 1
#                 if temp_paran_count == 0:
#                     temp_i = i
#                     break
#             temp_bool = False
#             x = temp_storage[temp_i+1:].split(' ')
#             if x[0].count('(') > 0:
#                 temp_bool = True
#             self.param1 = se(temp_storage[:temp_i+1], temp_bool)
#             print(temp_i)
#         print(self.operator, temp_storage, is_next_small_se)
        
#         for i in range(len(string)):
#             if i is '(':
#                 temp_paran_count += 1
#             else:
#                 pass

# def wrapper_se(string):
#     is_next_small_se = False
#     if string.split(' ')[1].count('(') > 0:
#         is_next_small_se = True
#     return se(string, is_next_small_se)

# se_obj = wrapper_se(test_string)
# se_obj = wrapper_se(test_string1)
# se_obj = wrapper_se(test_string2)
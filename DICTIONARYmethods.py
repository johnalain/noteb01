# # ====== dictionary methods ========== 
# # copy() - clear() - fromkeys() - items() - get() - keys() - pop() - values() - update() - setdefault() - popitem()
# original = {'a':2**2, 'b':2}
# shallow_copy =original.copy()
# print(shallow_copy)
# print(shallow_copy is original)

# original = {"a": 1, "b": 2}
# shallow_copy = {**original}
# print(original)
# print(shallow_copy)

# import copy
# #use .deep_copy if nested dictionary
# original = {"a": 1, "b": {"x": 10, "y": 20}}
# deep_copy = copy.deepcopy(original)

# deep_copy["b"]["x"] = 99
# print(original)   # {'a': 1, 'b': {'x': 10, 'y': 20}}
# print(deep_copy)  # {'a': 1, 'b': {'x': 99, 'y': 20}}

# keys = ["x", "y", "z"]
# new_dict = dict.fromkeys(keys)
# print(new_dict)
# Output: {'x': None, 'y': None, 'z': None} none is default value

# keys = ["x", "y", "z"]
# new_dict = dict.fromkeys(keys,2)
# print(new_dict)

# my_dict = {"a": 4, "b": 2, "c": 3}
# items_view = my_dict.items()

# print(items_view)  
# dict_items([('a', 1), ('b', 2), ('c', 3)])

# my_dict = {"a": 1, "b": 2, "c": 3}
# items_view = my_dict.items()

# print(items_view)  
# dict_items([('a', 1), ('b', 2), ('c', 3)])
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)





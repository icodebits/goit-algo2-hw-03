import csv
import timeit
from BTrees.OOBTree import OOBTree

# Завантаження даних з CSV
def load_data(filename):
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['ID'] = int(row['ID'])
            row['Price'] = float(row['Price'])
            data.append(row)
    return data

# Додавання товарів
def add_item_to_tree(tree, item):
    tree[item['ID']] = item

def add_item_to_dict(dictionary, item):
    dictionary[item['ID']] = item

# Діапазонний запит
def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items(min_price, max_price)]

def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item['Price'] <= max_price]

# Завантаження даних
data = load_data('generated_items_data.csv')

# Ініціалізація
oobtree = OOBTree()
dictionary = {}

# Додавання товарів
for item in data:
    add_item_to_tree(oobtree, item)
    add_item_to_dict(dictionary, item)

# Діапазон для тесту
min_price, max_price = 10, 50

# Вимірювання часу для OOBTree
oobtree_time = timeit.timeit(lambda: range_query_tree(oobtree, min_price, max_price), number=100)

# Вимірювання часу для Dict
dict_time = timeit.timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=100)

# Вивід результатів
print(f"Total range_query time for OOBTree: {oobtree_time:.6f} seconds")
print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

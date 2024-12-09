def find_item_index(products_list, item_to_find):
    if item_to_find in products_list:
        return products_list.index(item_to_find)
    else:
        return None

# Пример использования
products = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

items_to_search = ['банан', 'груша', 'персик']
for item in items_to_search:
    index = find_item_index(products, item)
    if index is not None:
        print('Первое вхождение товара', item, 'имеет индекс', index)
    else:
        print('Товар', item, 'не найден в списке')

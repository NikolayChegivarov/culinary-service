
def my_cook_book():
    with open('recipes.txt', encoding='utf-8') as file:
        dishes = {}  # Блюда
        for line in file.read().split('\n\n'):
            ingredients_quantity = []  # ингридиенты количество
            name, *ingredients = line.split('\n')
            for ingredient in ingredients[1:]:
                ingredient_name, quantity, measure = ingredient.split('|')
                ingredients_quantity.append(
                          {
                              'ingredient_name': ingredient_name,
                              'quantity': int(quantity),
                              'measure': measure
                          }
                      )
                dishes[name] = ingredients_quantity
        return dishes
# print(my_cook_book())

cook_book = my_cook_book()
# print(type(cook_book))

def get_shop_list_by_dishes(dishes, person_count):
    counted_list = {}
    for dish in dishes:
        if dish in cook_book:
            for i in cook_book[dish]:
                ingredient_name = i['ingredient_name']
                quantity = i['quantity'] * person_count
                if ingredient_name in counted_list:
                    counted_list[ingredient_name]['quantity'] += quantity
                else:
                    counted_list[ingredient_name] = {'measure': i['measure'], 'quantity': quantity}

    return counted_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


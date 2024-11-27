cook_book = {}

with open('rec.txt', 'r', encoding='utf-8') as rec:
    cook_book = {}
    for r in rec:
        dish_name = r.strip()
        ingredients_count = rec.readline()
        ingredients = []
        for n in range(int(ingredients_count)):
            recipes = rec.readline().strip().split(' | ')
            ingredient_name, quantity, measure = recipes
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
        rec.readline()
        cook_book[dish_name] = ingredients
       



def get_shop_list_by_dishes(dishes, person_count):
    ingr_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                if ingr['ingredient_name'] in ingr_dict:
                    ingr_dict[ingr['ingredient_name']]['quantity'] += ingr['quantity'] * person_count
                else:
                    ingr_dict[ingr['ingredient_name']] = {'measure': ingr['measure'],'quantity': (ingr['quantity'] * person_count)}
        else:
            print('Не знаем как приготовить =(')
    print(ingr_dict)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
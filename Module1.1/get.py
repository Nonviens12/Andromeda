def get_order(ingredients):
    order = []
    for ingredient in ingredients:
        command = input(f"Добавить {ingredient}? y/n: ")
        if command == "y":
            order.append(ingredient)
            print(f"Ингредиент '{ingredient}' добален!")
    return order



import time


def get_order(ingredients):
    order = []
    for ingredient in ingredients:
        command = input(f"Добавить {ingredient}? y/n: ")
        if command == "y" or command =="yes" \
        or command == "Y" or command =="Yes":
            order.append(ingredient)
            print(f"Ингредиент '{ingredient}' добален!")
    return order

def check_order(order):
    print("Подтвердите заказ:")
    print("Состав:",*order)
    print("y/n?")
    command = input()
    
    if command == "y":
        return True
    return False


print("Добрый вечер, это пиццерия!")
print("Выберете нужные вам ингредиенты и сделайте свой рецепт!")


while True:
    ingredients = ["Tomates", "mushrooms", "chise", "sausage", "olives", "strawberi"]
    order = get_order(ingredients)
    if check_order(order):
        print("Ваша пицца будет готова через 6 мин! Ожидайте заказ!")
        break
time.sleep(6)
print("Ваша пицца готова! Спасибо за заказ!")

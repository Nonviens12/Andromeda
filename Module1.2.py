import pickle

class Fish:

    def __init__(self, position=(0, 0), color='red'):
        self.position = position
        self.color = color

    def swim(self, x, y): #плавать
        self.position = (self.position[0] + x, 
                         self.position[1] + y)

    def get_position(self): #узнать где находится
        return self.position

    def __str__(self) -> str: # вывести string с информацией о рыбе
        return(f'Я - рыба {self.color} цвета,\
 нахожусь на позиции {self.position}')

fish1 = Fish(color='blue')





with open('output.txt', 'w') as inp:
    for i in range(10):
        inp.write('a'*i + '\n')
    inp.write('something\n')
    inp.write('Hello')

fp = open('output.txt', 'r')
print(fp.read())
fp.close()
















# with open('fish1.pkl', 'wb') as out:
#     pickle.dump(fish1, out, pickle.HIGHEST_PROTOCOL)

# with open('fish1.pkl', 'rb') as inp:
#     fish_loaded = pickle.load(inp)
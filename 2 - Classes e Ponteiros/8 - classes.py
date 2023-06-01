class Cookie:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color
    
cookie_one = Cookie('verde') # self é cookie_one
cookie_two = Cookie('azul') # self é cookie_two

print(f'Cookie_one é {cookie_one.get_color()}')
print(f'Cookie_two é {cookie_two.get_color()}')

cookie_one.set_color('amarelo')

print(f'\nCookie_one agora é {cookie_one.get_color()}')
print(f'Cookie_two ainda é {cookie_two.get_color()}')
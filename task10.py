class Discriminant:
    def discriminant(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def value_print(self):
        return f'Перше значення: {self.a}, Друге значення: {self.b}, Третє значення: {self.c}'

    def calculation(self):
        D = self.b**2-4*self.a*self.c
        if D > 0:
            x1 = int((-self.b - D**0.5)/(2*self.a))
            x2 = int((-self.b + D**0.5))/(2*self.a)
            return f'Перший корінь: {x1}, Другий корінь: {x2}'
        elif D == 0:
            x = int((-self.b)/2*self.a)
            return f"Один корінь: {x}"
        else:
            return f"Дискримінант коренів немає"

    def __str__(self):
        roots = self.calculation()
        return f"Квадратне рівняння: {self.a}x^2 + {self.b}x + {self.c} = 0\nРозв'язки: {roots}"

disc = Discriminant()
a = int(input("Введіть перше значення: "))
b = int(input("Введіть друге значення: "))
c = int(input("Введіть третє значення: "))
disc.discriminant(a,b,c)
print(disc)
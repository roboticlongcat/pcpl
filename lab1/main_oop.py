import sys

class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if self.a == 0:
            print("A не должен быть равен 0. Уравнение не может быть решено!")
            return []
        discriminant = self.b ** 2 - 4 * self.a * self.c
        roots = []
        if discriminant > 0:
            z1 = (-self.b + discriminant ** 0.5) / (2 * self.a)
            z2 = (-self.b - discriminant ** 0.5) / (2 * self.a)
            if z1 >= 0:
                roots.append(z1 ** 0.5)
                roots.append(-(z1 ** 0.5))
            if z2 >= 0:
                roots.append(z2 ** 0.5)
                roots.append(-(z2 ** 0.5))
        if discriminant == 0:
            z = -self.b / (2 * self.a)
            if z >= 0:
                roots.append(z ** 0.5)
                roots.append(-(z ** 0.5))
        if len(roots):
            roots = sorted(set(roots))
        return roots

def main():
    coef = []
    input_flag = True
    if len(sys.argv) == 4:
        try:
            for i in range(1, 4):
                n = float(sys.argv[i])
                coef.append(n)
            input_flag = False
        except ValueError:
            print("Один или несколько параметров командной строки некорректны.")
    while input_flag:
        try:
            for i in range(1, 4):
                n = float(input("Введите коэффициент:"))
                coef.append(n)
            input_flag = False
        except ValueError:
            print('Введите число!')

    equation = BiquadraticEquation(coef[0], coef[1], coef[2])
    solution = equation.solve()
    if len(solution) > 1:
        print("Действительные корни уравнения:", *solution)
    elif len(solution) == 1:
        print("Единственный действительный корень уравнения:", solution[0])
    else:
        print("Действительных корней нет.")

if __name__ == '__main__':
    main()

import sys

def get_coef():
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
    return coef

def solve(a, b, c):
    if a == 0:
        print("A не должен быть равен 0. Уравнение не может быть решено!")
        return []
    discriminant = b ** 2 - 4 * a * c
    roots = []
    if discriminant > 0:
        z1 = (-b + discriminant ** 0.5) / (2 * a)
        z2 = (-b - discriminant ** 0.5) / (2 * a)
        if z1 >= 0:
            roots.append(z1 ** 0.5)
            roots.append(-(z1 ** 0.5))
        if z2 >= 0:
            roots.append(z2 ** 0.5)
            roots.append(-(z2 ** 0.5))
    if discriminant == 0:
        z = -b / (2 * a)
        if z >= 0:
            roots.append(z ** 0.5)
            roots.append(-(z ** 0.5))
    if len(roots):
        roots = sorted(set(roots))
    return roots

def analyse(sol):
    if len(sol) > 1:
        print("Действительные корни уравнения:", *sol)
    elif len(sol) == 1:
        print("Единственный действительный корень уравнения:", sol[0])
    else:
        print("Действительных корней нет.")

def main():
    a, b, c = get_coef()
    solution = solve(a, b, c)
    analyse(solution)

if __name__ == '__main__':
    main()
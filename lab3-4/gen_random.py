from random import randint

def gen_random(num_count, begin, end):
    random = [randint(begin, end) for i in range(num_count)]
    return random

def main():
    random = gen_random(5, 1, 3)
    print(*random, sep=', ')

if __name__ == '__main__':
    main()
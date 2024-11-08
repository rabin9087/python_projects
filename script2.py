from script1 import *


def favorite_drink(drink):
    print(f"{drink}")

def main():
    print("this is script2")
    favorite_food("Momo")
    favorite_drink("tea")

if __name__ == '__main__':
    main()
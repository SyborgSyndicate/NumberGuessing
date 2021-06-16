#python number guesing
import os, sys, time, random
def main():
    x = random.randint(1, 10)
    print("Tebaklah angka 1-10")
    try:
        j = int(input("Tebak: "))
        if j == x:
            print('benar')
        else:
            print('salah! angka yang benar adalah', x)
    except ValueError:
        main()
if __name__ == "__main__":
    main()
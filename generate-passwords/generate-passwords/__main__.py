from utils import Randomizer


def main():
    password = Randomizer('low')
    print(password.generate_password(20))


if __name__ == '__main__':
    main()

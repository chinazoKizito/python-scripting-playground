from random import randint

answer = randint(1, 10)


def run_guess(guess, number):
    if 0 < guess < 11:
        if guess == number:
            print("You are a genius numbers match!!!")
            return True
    else:
        print('Hey I said numbers from 1~10')
        return False


if __name__ == '__main__':
    while True:
        try:
            user_guess = int(input("Enter a number from 1~10: "))
            if run_guess(guess=user_guess, number=answer):
                break
        except ValueError:
            print('Please enter a number')

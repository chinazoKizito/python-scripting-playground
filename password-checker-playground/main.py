import requests
import hashlib
import sys


# This module reads password from a text file and checks if pawned (safer)

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error Fetching: {res.status_code}, Check the API and try again")
    return res


def get_password_leaks_count(hashes, hash_to_check):
    # Splits password into a tuple of  hash and count
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        # if hash equal to our tail return how many times, else 0
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_characters, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_5_characters)
    return get_password_leaks_count(response, tail)


def main(args):
    for file in args:
        if file.endswith('.txt'):
            with open(file) as my_file:
                password = my_file.read()
                count = pwned_api_check(password)
                if count:
                    print(f"{password}, was found {count} times.... You should probably change your password")
                else:
                    print(f"{password} was NOT found, carry on!")
        else:
            print('Arguments are not text file, Run python check_my_password.py instead to work directly with your '
                  'passwords in the command line')
    return 'Done'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

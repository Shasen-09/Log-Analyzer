from functools import wraps
import time

is_logged_in = False


def login():
    global is_logged_in
    name = input("Enter your name: ")
    if name == "Shasen":
        is_logged_in = True
    else:
        print("Credentials do not match")


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Calculation took {end - start:.6f} seconds")
        return result

    return wrapper


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            result = func(*args, **kwargs)
            return result
        else:
            print("Log in first")
    return wrapper


@decorator
def view_balance():
    print("Your balance is 0. You are fakir!")


@decorator
def topup_wallet(amount):
    print(f"Your esewa load is succesful!{amount}")


@decorator
def profile(name, contact):
    """---This is a learning module---"""
    print(f"Account holder's name: {name} ")
    print(f"Contact: {contact}")


def log_out():
    global is_logged_in
    is_logged_in = False
    return


@timer
def login_time():
    time.sleep(2)
    return (sum(range(100000)))


data = {
    "name": "Shasen",
    "contact": 9745967860
}

# login()
# view_balance()


# print(profile.__annotations__)
# print(view_balance.__name__)

print(login_time())

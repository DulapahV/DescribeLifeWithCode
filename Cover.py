def do_something():
    pass

def try_again():
    pass

class Fail(Exception):
    pass


try:
    do_something()
except Fail:
    try_again()
finally:
    print("Success!")
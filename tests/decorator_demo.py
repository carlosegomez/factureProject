import functools
import requests
import time


def debug(active=True):
    def nested(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if active:
                print('function', function.__name__)
                print("args:", args)
                print("kwargs", kwargs)
                print(result)
            return result
        return wrapper
    return nested


#get_user = debug(active=True)(get_user)
#print(get_user())


def calc_time(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        stop = time.time()
        time_exe = stop - start
        return time_exe
    return wrapper


@calc_time
# @debug(True)
def get_user():
    response = requests.get('https://randomuser.me/api')
    return response.json()

print(get_user())



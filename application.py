import time


def main():
    print("This is a sample project to demonstrate unit tests and test automation.")


def num_max(arg1, arg2):
    """
    This function takes two arguments and returns the maximum. There are built-in methods for this but these are
    example functions.
    """
    return arg1 if arg1 > arg2 else arg2


def array_max(array):
    """
    Return maximum value in an array.
    """
    result = array[0]
    for each in array:
        result = each if each > result else result
    return result


def is_valid(credentials):
    """
    boolean credentials checker
    """
    if credentials == "test": return True
    return False


def current_data():
    """ Function gets a data set. """
    result = {
        "time": time.time(),
        "gps": (45.5097037, -122.6813361),
        "temp": 73.0,
        "humidity": 54.4,
        "leaf wetness": .20110
    }
    return result


def current_data_bad_response():
    """ uh oh, something went wrong!"""
    raise ConnectionAbortedError


def get_data():
    try:
        return current_data_bad_response()
    except ConnectionAbortedError as ex:
        print("Error: connection aborted")
        ''' Magic retry logic'''
    finally:
        print("Closing connection")
        ''' Magic connection closer '''

if __name__ == '__main__':
    main()

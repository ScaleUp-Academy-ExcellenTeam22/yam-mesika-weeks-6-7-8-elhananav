def group_by(func, iterable):
    """
    Gets a function as the first parameter, and iterable as the second parameter.
    The function will return a dictionary, in which: The keys are the values
    returned from the function passed as the first parameter. The value corresponding
    to a particular key is a list of all the organs for which the value appearing in
    the key is repeated.
    :param func: The function to run on the iterables
    :param iterable: The values for the dictionary
    :return: Dictionary as described above
    """
    dictionary = {}
    for item in iterable:
        dictionary.setdefault(func(item), []).append(item)
    return dictionary


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))

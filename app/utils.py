from fake_db import db

stack = []
results = []


def flatten(db: list) -> list:
    """
    Recursive function that parses multilevel lists and dictionaries
    :param db: list
    :return results: flatten list with integer and float

    Output:
    [[50.2], [62], [20.2], [50.2], [10.5], [1], [2], [3], [1]]
    """
    try:
        for item in db:
            for key, value in item.items():
                if isinstance(value, dict):
                    # call recursive function for dictionaries
                    flatten([value])
                elif isinstance(value, (int, float)):
                    # ----------------
                    # action with item
                    # ----------------
                    stack.append([value])
                elif isinstance(value, list):
                    def read_list(obj):
                        for v in obj:
                            if isinstance(v, list):
                                print(len(v), v, type(v))
                                # call recursive function for lists
                                read_list(v)
                            elif isinstance(v, (int, float)):
                                stack.append([v])

                    if len(value) >= 1:
                        # ----------------
                        # action with item
                        # ----------------
                        read_list(value)

    except AttributeError as e:
        print(e)
    finally:
        print('stack', stack)
        return stack


def calculate_sum(items: list) -> int:
    """
    :param items: list of integers
    :return integer: as calculated results from all items
    """
    total_sum = int((sum([x for x in (y for x in items for y in x)])))
    print('total_sum', total_sum)
    return total_sum


def calculate_results(data: list) -> list:
    """

    :param data: list
    :return: add total sum for all integers from data and return
    new dict with key 'total_sum'
    """
    flatten_data = flatten(data)
    total_sum = calculate_sum(flatten_data)
    data.append({'total_sum': total_sum})
    return data

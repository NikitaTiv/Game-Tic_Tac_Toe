def separate_list(objects_list, lenght):
    for i in range(0, len(objects_list), lenght):
        yield objects_list[i : i + lenght]


def convert_iteration_to_list(obj):
    return list(obj)


def repeat_on_fail(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)
            except (ValueError, IndexError) as e:
                print(e)
                continue
            else:
                break

    return wrapper
def separate_list(objects_list, lenght):
    for i in range(0, len(objects_list), lenght):
        yield objects_list[i : i + lenght]


def convert_iteration_to_list(obj):
    return list(obj)

def break_list_to_chunks(lst, chunk_size):
    # result = []
    # start = 0
    # for i in range(chunk_size):
    #     result.append(lst[start:chunk_size + start])
    #     start += chunk_size
    #
    # return result
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


# [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10]]
print(break_list_to_chunks(list(range(11)), 4))

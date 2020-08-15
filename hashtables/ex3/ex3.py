def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    flat_arr = [num for sub_arr in arrays for num in sub_arr]

    count_dict = {}
    for num in flat_arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    return [item[0] for item in count_dict.items() if item[1] == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

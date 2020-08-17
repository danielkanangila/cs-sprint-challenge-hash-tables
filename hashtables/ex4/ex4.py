def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    a_dict = {}

    for i in range(len(a)):
        if abs(a[i]) in a_dict:
            a_dict[abs(a[i])] += 1
        else:
            a_dict[abs(a[i])] = 1

    result = [item[0] for item in a_dict.items() if item[1] >= 2]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

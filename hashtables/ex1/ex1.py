def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weights_dict = {}

    for i in range(length):
        weights_dict[weights[i]] = i

    for index in range(0, length):

        if limit - weights[index] in weights_dict:
            index2 = weights_dict[limit - weights[index]]
            result = [index, index2]
            result.sort(reverse=True)
            return tuple(result)

    return None

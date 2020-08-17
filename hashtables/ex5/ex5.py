# Your code here
from os import path


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    files_dict = {}

    for file in files:
        filename = path.basename(file)
        if filename in files_dict:
            files_dict[filename].append(file)
        else:
            files_dict[filename] = [file]

    result = []
    for query in queries:
        if query in files_dict:
            result = [*result, *files_dict[query]]
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

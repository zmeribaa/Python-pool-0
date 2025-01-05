def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function
    is true. If function is None, return the items that are true."""
    if function is None:
        return iter([item for item in iterable if bool(item)])
    return iter([item for item in iterable if function(item)])


def main():
    try:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = ft_filter(lambda x: x % 2 == 0, numbers)
        print("Even numbers:", list(result))

        mixed_values = [0, 1, False, True, "", "hello", [], [1, 2]]
        result = ft_filter(None, mixed_values)
        print("Truthy values:", list(result))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

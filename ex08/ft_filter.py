
def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items that
    are true."""
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item


def main() -> None:
    """Test the ft_filter function."""
    numbers = range(10)
    result = list(ft_filter(lambda x: x % 2 == 0, numbers))
    print(result)


if __name__ == "__main__":
    main()

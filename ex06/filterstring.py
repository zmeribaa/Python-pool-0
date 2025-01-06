import sys
from ft_filter import ft_filter


def main():
    """Program that filters words from a string based on their length."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        string = sys.argv[1]
        assert isinstance(string, str), "the arguments are bad"
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = string.split()
        result = list(ft_filter(lambda x: len(x) > n, words))
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"AssertionError: the arguments are bad {e}")


if __name__ == "__main__":
    main()

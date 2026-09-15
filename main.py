import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 wheel_auditor.py first.whl second.whl")
        return 2

    try:
        with open(sys.argv[1], "rb") as file:
            first = file.read()
        with open(sys.argv[2], "rb") as file:
            second = file.read()
    except OSError as error:
        print("Could not read a file:", error)
        return 2

    if first == second:
        print("PASS: The wheel files are identical.")
        return 0

    print("FAIL: The wheel files are different.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

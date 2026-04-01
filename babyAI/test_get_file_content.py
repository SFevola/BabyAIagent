from functions.get_file_content import get_file_content


def test():
    result = get_file_content("calculator", "main.py")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(result)


if __name__ == "__main__":
    test()


# from functions.get_file_content import get_file_content

# #print(get_file_content("calculator", "lorem.txt"))

# def test():
#     result = get_file_content("calculator", "lorem.txt")
#     print(f"Lorem length: {len(result)}")
#     print(result[-100:])  # just print the tail to check the truncation message

#     result = get_file_content("calculator", "main.py")
#     print("Result for main.py:")
#     print(result)
#     print("")

#     result = get_file_content("calculator", "pkg/calculator.py")
#     print("Result for 'pkg/calculator.py' directory:")
#     print(result)

#     result = get_file_content("calculator", "/bin/cat")
#     print("Result for '/bin/cat.py' directory:")
#     print(result)

#     result = get_file_content("calculator", "pkg/does_not_exist.py")
#     print("Result for 'pkg/does_not_exist.py' directory:")
#     print(result)


# if __name__ == "__main__":
#     test()

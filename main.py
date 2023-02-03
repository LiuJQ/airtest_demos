# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print('hello, world')
    print('hello,', 'this is jackin,', 'and you ?')
    name = input('jackin is waiting for you: ')
    print(f'hello, I am {name}')
    print(f"hello, I'm {name}, nice to meet you.")
    print('''line1\nline2\nline3''')
    print('''line1
line2
line3''')

    age = int(input(f'hello {name}, how old are you ? tell me: '))
    if age >= 18:
        print(f'{name} is an adult')
    else:
        print(f'{name} is a teenager')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

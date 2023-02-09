# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def filter_devices(devices):
    offline = []
    remote = []
    for d in devices:
        print(f"device: {d[0]}, status: {d[1]}")
        if d[1].find("offline") != -1:
            offline.append(d[0])
        if d[0].find(":") != -1:
            remote.append(d[0])
    print(f"offline devices: {offline}")
    print(f"remote devices: {remote}")


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

    deviceList = [('8TC6Z545EIJR45YL', 'offline'), ('SSSCNFTWZLHIY9ZX', 'device'), ('10.103.5.31:5555', 'offline'),
                  ('10.103.5.32:5555', 'device')]
    filter_devices(deviceList)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

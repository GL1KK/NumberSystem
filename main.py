def to_binary_number_system():
    print("Введите число:")
    value = int(input())
    binary = []
    while True:
        division = int(value / 2)
        remains = value % 2 
        binary.append(str(remains))
        value = division
        if division == 0:
            break
    print(''.join(reversed(binary)))
def to_octal_number_system():
    print("Введите число:")
    value = int(input())
    octal = []
    while True:
        division = int(value / 8)
        remains = value % 8
        octal.append(str(remains))
        value = division
        if division == 0:
            break
    print(''.join(reversed(octal)))
def to_decimal_number_system():
    print("В какую систему счисления?(1 - восьмиричная, 2 - бинарная, 3 - шеснадцатиричная)")
    action = input()
    match action:
        case "1":
            octal()
        case "2":
            binary()
        case "3":
            hex()
def octal():
    print("Введите число:")
    value = input()
    octal_str = str(value)
    decimal_list = []
    decimal = 0
    degree = 0
    for i in reversed(octal_str):
        decimal = int(i) * (8 ** degree) 
        decimal_list.append(decimal)
        degree += 1
    print(sum(decimal_list))
def binary():
    print("Введите число:")
    value = input()
    degree = 0
    binary_str = str(value)
    binary = 0
    binary_list = []
    for i in reversed(binary_str):
        binary = int(i) * (2 ** degree) 
        binary_list.append(binary)
        degree += 1
    print(sum(binary_list))
def hex():
    print("Введите число:")
    value = input()
    degree = 0
    hex_str = str(value)
    hex_list = []
    list_hex = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}
    for i in reversed(hex_str):
        if i in list_hex:
            i = list_hex[str(i)]
        hex_val = int(i) * (16 ** degree)
        hex_list.append(hex_val)
        degree += 1
    print(sum(hex_list))
def to_hexadecimal_number_system():
    print("Введите число:")
    value = input()
    hexadecimal_list = []
    list_hex = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
    while True:
        division = int(value / 16)
        remains = value % 16
        if str(remains) in list_hex:
            remains = list_hex[str(remains)] 
        hexadecimal_list.append(str(remains))
        value = division
        if division == 0:
            break
    print(''.join(reversed(hexadecimal_list)))

def main():
    while True:
        print("Что выберите?(1 - в бинарную(из десячиной), 2 - в восьмиричную(из десячиной), 3 - в десячную, 4 - в шеснадцатиричную(из десячиной), 5/q - выход)")
        action = input()
        match action:
            case "1":
                to_binary_number_system()
            case "2":
                to_octal_number_system()
            case "3":
                to_decimal_number_system()
            case "4":
                to_hexadecimal_number_system()
            case "5":
                break
            case "q":
                break
        
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Ошибка! {e}")
        main()
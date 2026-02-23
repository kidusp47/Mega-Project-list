def convert_to_decimal():
    values = [128, 64, 32, 16, 8, 4, 2, 1]
    new_values = []
    binary = input("please enter a binary number(should be 8 digits): ")
    if len(binary) != 8 or any(bit not in "01" for bit in binary):
        print("Invalid binary number! Must be exactly 8 digits of 0s and 1s.")
        return
    else:
        binary_list = list(binary)
        for i in range(len(binary_list)):
            if binary_list[i] == "1":
                new_values.append(values[i])
        print(f"{binary} is {sum(new_values)} in decimal format")

def convert_to_binary():
    binary_values = []
    decimal = int(input("please enter a number(0 < x < 256): "))
    dec_values =decimal
    if decimal < 0 or decimal > 255:
        print("Invalid number! Must be between 0 and 255.")
    else:
        for i in range(8):
            binary_values.append(decimal % 2)
            decimal = decimal//2
        binary_values.reverse()
        final = "".join(map(str, binary_values))
        print(f"{dec_values} is {final} in binary format.")

convert = input("type 'binary' to convert to decimal to binary type 'decimal' to convert binary to decimal: ").lower()
if convert == "binary":
    convert_to_binary()
elif convert == "decimal":
    convert_to_decimal()
else:
    print("Invalid input!")
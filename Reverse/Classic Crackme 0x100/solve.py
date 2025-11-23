def transform(s):
    s = list(s)
    length = len(s)

    for _ in range(3):  # repeat transformation 3 times
        for j in range(length):
            # identical bit-magic from the C code
            u = (((j % 0xFF) >> 1) & 0x55) + ((j % 0xFF) & 0x55)
            u = ((u >> 2) & 0x33) + (u & 0x33)
            v = ((u >> 4) & 0xF) + (u & 0xF)

            t = (ord(s[j]) - ord('a') + v) % 26
            s[j] = chr(ord('a') + t)

    return "".join(s)


def main():
    output = "mpknnphjngbhgzydttvkahppevhkmpwgdzxsykkokriepfnrdm"

    user_input = input("Enter the secret password: ").strip()

    # must be same length as output
    user_input = user_input.lower()
    if len(user_input) != len(output):
        print("FAILED!")
        return

    transformed = transform(user_input)

    if transformed == output:
        print("SUCCESS! Here is your flag: picoCTF{sample_flag}")
    else:
        print("FAILED!")


if __name__ == "__main__":
    main()

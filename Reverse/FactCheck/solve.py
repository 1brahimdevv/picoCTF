def build_flag():
    flag = "picoCTF{wELF_d0N3_mate_"

    local_228 = "4"
    local_208 = "5"
    local_1e8 = "6"
    local_1c8 = "3"
    local_1a8 = "e"
    local_188 = "5"
    local_168 = "a"
    local_148 = "e"
    local_128 = "e"
    local_108 = "d"
    local_e8 = "b"
    local_c8 = "f"
    local_a8 = "6"
    local_88 = "e"
    local_68 = "d"
    local_48 = "8"

    # شرط 1
    if local_208[0] < 'B':   # '5' < 'B' → True
        flag += local_c8     # "f"

    # شرط 2
    if local_a8[0] != 'A':   # '6' != 'A' → True
        flag += local_68     # "d"

    # شرط 3 (false)
    if ord(local_1c8[0]) - ord(local_148[0]) == 3:   # '3' - 'e' → False
        flag += local_1c8

    # باقي الإضافات
    flag += local_1e8
    flag += local_188

    if local_168[0] == 'G':  # False
        flag += local_168

    flag += local_1a8
    flag += local_88
    flag += local_228
    flag += local_128
    flag += "}"

    return flag


print(build_flag())

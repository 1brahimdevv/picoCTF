# picoCTF Reverse Engineering Write-up

## Overview
We analyze a compiled binary using Ghidra, extract the password transformation logic, reverse it, and then connect using `nc` to retrieve the flag.

---

## Step 1 — Load the Binary in Ghidra
1. Open Ghidra.
2. Import the challenge binary.
3. Let Ghidra analyze it.
4. Open the `main()` function in the decompiler.

---

## Step 2 — Analyze the Code
Inside `main()` we find:

- A hardcoded output string:
```mpknnphjngbhgzydttvkahppevhkmpwgdzxsykkokriepfnrdm```

- The program asks for a password.
- It transforms the user input *three times* using a deterministic per-character shift based on the index.
- It compares:

```c
memcmp(input, output, len)
```

##Recovered Password
```mmhhkjbakavyaqprqnpbuygdymyyddkratrjsbbceizsgtbcxd```

###Run
```nc titan.picoctf.net 60592```

Enter the ```mmhhkjbakavyaqprqnpbuygdymyyddkratrjsbbceizsgtbcxd```


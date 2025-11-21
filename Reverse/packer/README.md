
# picoCTF – Packer (Reverse Engineering · Easy)

Below are the steps used to solve the challenge.

---

## 🛠️ Step 1 — Inspecting the File Using `strings`

We start by running `strings` on the downloaded file to check for hints:

```bash
strings out
````

Inside the output, we found:

```
UPX!
UPX!
```

This indicates the file is packed with **UPX**.

---

## 📦 Step 2 — Unpacking the File with UPX

To decompress the packed binary, we used:

```bash
upx -d out -o outofupx
```

This created an unpacked executable named `outofupx`.

---

## 🔬 Step 3 — Analyzing the Unpacked File in Ghidra

We opened `outofupx` in **Ghidra**.
Inside the decompiled `main` function, we found that the password used by the program is stored in **hex-encoded form** rather than plaintext.

---

## 🧮 Step 4 — Decoding the Hex Password

We copied the hex string from the binary and decoded it using a hex-to-text tool (like CyberChef).
Decoding the hex provided us with the correct **flag**.

```

---



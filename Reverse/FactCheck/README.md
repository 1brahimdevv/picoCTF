# 🧩 picoCTF ELF Reversing — Solution Explanation

## 📌 Overview
To solve this picoCTF challenge, we opened the ELF binary in **Ghidra** to analyze the `main()` function after decompilation.  
Inside the `main()` function, we saw that the program constructs the flag step-by-step using multiple string variables and a series of `if` statements that determine the rest of the flag.

After understanding the logic, we rewrote the same behavior in **Python**, allowing us to run a simple script (`solve.py`) to automatically generate the final flag without executing the binary.

---

## 🛠️ Steps to Solve

### **1️⃣ Decompile the Binary Using Ghidra**
After loading the file into Ghidra, we navigated to the `main()` function.  
We observed that the flag begins with:```picoCTF{wELF_d0N3_mate_```



The remaining characters are appended conditionally based on several `if` statements.

---

### **2️⃣ Translate the Logic Into Python**
We recreated all variable assignments and conditions in Python so that the script behaves exactly like the original C++ logic.

Running the Python script (`solve.py`) produces the full flag.

---

## 🧪 Example Output

Running:

```python3 solve.py```


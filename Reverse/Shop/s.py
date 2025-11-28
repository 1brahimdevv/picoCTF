import base64
import itertools
import string

s = b"PjavkptB2tPNbBJewQBD/KlDP1g_fpBnKyhti11wQ/JIWBEgtPAt3YPE6g8qd7/pWlMkjZuAYGqbSv46xuR"

print("Raw:", s)

# ---------- Try base64 variants ----------
def try_b64(x):
    for pad in range(4):
        try:
            print("b64:", base64.b64decode(x + b"="*pad))
        except:
            pass

try_b64(s)

# ---------- Try XOR brute force ----------
print("\n[XOR brute force]")
for key in range(256):
    out = bytes([b ^ key for b in s])
    if all(32 <= c <= 126 for c in out):
        print(f"key {key:02X}: {out}")

# ---------- Caesar-shift printable-only ----------
print("\n[Caesar ASCII shift]")
for shift in range(256):
    out = bytes([(b + shift) % 256 for b in s])
    if all(32 <= c <= 126 for c in out):
        print(f"shift {shift}: {out}")

# ---------- Rotation of bytes ----------
print("\n[Byte rotation]")
for r in range(1,8):
    out = bytes([((b << r) | (b >> (8-r))) & 0xff for b in s])
    if all(32 <= c <= 126 for c in out):
        print("rotL", r, out)

    out = bytes([((b >> r) | (b << (8-r))) & 0xff for b in s])
    if all(32 <= c <= 126 for c in out):
        print("rotR", r, out)

# ---------- Ascii85 / Base85 ----------
print("\n[Ascii85/Base85]")
for decoder in [base64.a85decode, base64.b85decode]:
    try:
        print(decoder(s))
    except:
        pass

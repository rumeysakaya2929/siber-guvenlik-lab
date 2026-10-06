import hashlib
import time
from argon2 import PasswordHasher

parola = "ornek-parola-123"
parola_b = parola.encode()

# ---------- SHA-256 ----------
# Cok hizli oldugu icin 100.000 kez tekrar edip ortalama aliyoruz
N = 100_000
t0 = time.perf_counter()
for _ in range(N):
    hashlib.sha256(parola_b).digest()
sha_sure = (time.perf_counter() - t0) / N

# ---------- Argon2id ----------
ph = PasswordHasher()   # varsayilan: argon2id
M = 10
t0 = time.perf_counter()
for _ in range(M):
    ph.hash(parola)
arg_sure = (time.perf_counter() - t0) / M

print(f"SHA-256  : {sha_sure * 1e6:.2f} mikrosaniye / hash")
print(f"Argon2id : {arg_sure * 1e3:.2f} milisaniye / hash")
print(f"Oran     : Argon2id yaklasik {arg_sure / sha_sure:,.0f} kat daha yavas")
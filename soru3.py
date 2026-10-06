from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag
import os

# ---------- A) CTR: anahtarsız mesaj değiştirme ----------
print("=== A) CTR ===")
key = os.urandom(16)
nonce = os.urandom(16)
mesaj = b"Tutar: 100 TL"

enc = Cipher(algorithms.AES(key), modes.CTR(nonce)).encryptor()
sifreli = enc.update(mesaj) + enc.finalize()
print("Orijinal mesaj :", mesaj)

# Saldirgan: anahtari bilmiyor, sadece sifreli veriyi degistiriyor
saldiri = bytearray(sifreli)
poz = 7                                  # "1" karakterinin indeksi
saldiri[poz] ^= ord("1") ^ ord("9")      # 1 -> 9

# Alici: normal sekilde cozuyor
dec = Cipher(algorithms.AES(key), modes.CTR(nonce)).decryptor()
sonuc = dec.update(bytes(saldiri)) + dec.finalize()
print("Alicinin gordugu:", sonuc)        # b'Tutar: 900 TL'

# ---------- B) AES-GCM: ayni saldiri ----------
print("\n=== B) AES-GCM ===")
aes = AESGCM(AESGCM.generate_key(bit_length=128))
nonce = os.urandom(12)
sifreli = aes.encrypt(nonce, b"Tutar: 100 TL", None)

saldiri = bytearray(sifreli)
saldiri[7] ^= ord("1") ^ ord("9")

try:
    aes.decrypt(nonce, bytes(saldiri), None)
    print("Mesaj cozuldu (olmamaliydi!)")
except InvalidTag:
    print("Degisiklik tespit edildi! (InvalidTag)")
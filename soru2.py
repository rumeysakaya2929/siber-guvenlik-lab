from PIL import Image
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

img = Image.open("resim.png").convert("RGB")
w, h = img.size
ham = img.tobytes()                              # ham piksel baytları
dolgulu = ham + b"\x00" * ((-len(ham)) % 16)     # ECB için 16'nın katı

key = os.urandom(16)

def sifrele(mod):
    enc = Cipher(algorithms.AES(key), mod).encryptor()
    ct = enc.update(dolgulu) + enc.finalize()
    return Image.frombytes("RGB", (w, h), ct[:len(ham)])

ecb = sifrele(modes.ECB())
ctr = sifrele(modes.CTR(os.urandom(16)))

sonuc = Image.new("RGB", (w * 3, h))
sonuc.paste(img, (0, 0))
sonuc.paste(ecb, (w, 0))
sonuc.paste(ctr, (w * 2, 0))
sonuc.save("karsilastirma.png")
print("Bitti: karsilastirma.png olusturuldu")
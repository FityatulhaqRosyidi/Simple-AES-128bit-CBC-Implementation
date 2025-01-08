from utils import cbc_encrypt, cbc_decrypt
from key_manager import getKey, postKey
import os

def main() :
  print('='*90)
  print('Selamat datang di Program Sederhana Implementasi Algoritma Enkripsi AES-CBC.')
  print('='*90)

  while True :
    print("\nMasukkan Perintah")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print('3. Keluar')

    try :
      opt = int(input(">> "))

      if (opt == 1) :
        print('='*90)
        print('ENKRIPSI.')
        print('='*90)
        print()
        pt = input('Masukkan text yang ingin di enkripsi\n>> ').encode()
        key = os.urandom(16)
        iv = os.urandom(16)

        ct = cbc_encrypt(key, iv, pt)
        print(f'\nCiphertext : {ct.hex()}')
        print(f'Key : {key.hex()}')
        print(f'iv: {iv.hex()}\n')

        keyfilepath = input('Masukkan nama file untuk menyimpan kunci (tanpa .txt)\n>> ')
        postKey(keyfilepath, key.hex(), iv.hex())


      elif (opt == 2) :
        print('='*90)
        print('DEKRIPSI.')
        print('='*90)
        print()
        ct = input('Masukkan text yang ingin di dekripsi\n>> ')
        keyfilepath = input('Masukkan nama file kunci (tanpa .txt)\n>> ')
        key, iv = getKey(keyfilepath)
        pt = cbc_decrypt(bytes.fromhex(key),bytes.fromhex(iv), bytes.fromhex(ct))
        print(f'\nPlaintext : {pt}')
        print(f'Key : {key}')
        print(f'iv: {iv}\n')

      elif (opt == 3) :
        break

      else :
        print("Masukkan Salah, silahkan masukkan angka rentang 1-3!")

    except ValueError:
      print("Masukkan Salah, silahkan masukkan angka!")


if __name__ == "__main__" :
  main()
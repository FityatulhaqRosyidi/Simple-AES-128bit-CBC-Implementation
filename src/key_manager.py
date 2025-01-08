
def postKey(filename, key, iv) :
    with open(f'../keys/{filename}.txt', 'w') as file:
        file.write(f"{key}\n")
        file.write(f"{iv}\n")
    print(f"Key dan IV berhasil disimpan ke {filename}.txt")

def getKey(filename):
    with open(f'../keys/{filename}.txt', 'r') as file:
        lines = file.readlines()
    if len(lines) < 2:
        raise ValueError("File tidak berisi cukup data untuk key dan IV.")
    key = lines[0].strip()  
    iv = lines[1].strip()  
    return (key, iv)
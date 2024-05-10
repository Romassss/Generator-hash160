import os
import hashlib

def hash160(password):
    sha256 = hashlib.sha256(password.encode()).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).digest()
    return ripemd160.hex()

input_file = "Documents/txtEditor/qwe.txt"
output_folder = "Documents/txtEditor/hash160"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_file = os.path.join(output_folder, "hash.txt")

with open(input_file, 'r') as f_in:
    with open(output_file, 'w') as f_out:
        for line in f_in:
            password = line.strip()
            hashed_password = hash160(password)
            f_out.write(hashed_password + "\n")

print("Все пароли из файла qwe.txt успешно сконвертированы в hash160 и сохранены в файле hash.txt в папке hash160.")

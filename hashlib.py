import hashlib
from hashlib import sha256
import csv
import os
from collections import OrderedDict
def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name , 'r') as f:
        reader = csv.reader(f)
        with open(output_file_name , 'w') as g:
            my_dict = OrderedDict()
            for row in reader:
                name = row[0]
                password =str(row[1])
                for x in range(0, 10000):
                    four_digit=str(x).zfill(4)
                    hashednumber = hashlib.sha256(str(four_digit).encode('utf-8')).hexdigest()
                    my_dict[hashednumber] = four_digit
                if password in my_dict.keys():
                    pass1 = my_dict[password]
                g.write(name + "," + pass1 + '\n')
input_file_name = os.path.abspath("C:\\Users\\Mahsa\\Desktop\\Python\\jadi python\\hash_file_1.csv")
output_file_name = os.path.abspath("C:\\Users\\Mahsa\\Desktop\\Python\\jadi python\\output_file_1.csv")
hash_password_hack(input_file_name , output_file_name)
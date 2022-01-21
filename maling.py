import requests
import sys
import time
import os


# buat ngasih warna
red = '\033[91m'
green = '\033[92m'
white = '\033[00m'

#animasi loading
def load_animasi():    
    kata_str = "i am not a hacker i am just tester..."
    ls_len = len(kata_str) 
    animasi = "|/-\\"
    htganim = 0
    htgwaktu = 0        
    i = 0                     
    
    while (htgwaktu != 100): 
        time.sleep(0.075)  
        kata_str_list = list(kata_str)
        x = ord(kata_str_list[i]) 
        y = 0                             
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            kata_str_list[i]= chr(y) 
        res =''              

        for j in range(ls_len): 

            res = res + kata_str_list[j] 
        sys.stdout.write("\r"+res + animasi[htganim]) 
        sys.stdout.flush() 
        kata_str = res 
        htganim = (htganim + 1)% 4
        i =(i + 1)% ls_len 
        htgwaktu = htgwaktu + 1

# windows
    if os.name =="nt": 
        os.system("cls") 
# linux / Mac OS 
    else:
        os.system("clear") 
if __name__ == '__main__':  
    load_animasi()


print (green+'''

           1010010        0001101
           1000100        0011100
           0110011        1001001 
           1011001        0010111
           1010100        0100100
           1110010101011100010100
           101010000HADES01011100
           1010101000111000100001
           0011100        1000000
           1001000        0100100
           1010101        1000110
           1100110        0011100
           1010001        0011111

'''+white)
print( red+"   [-] I AM NOT HACKER, I AM JUST TESTER[-]"+white)

#input
print (red+"[•]Contoh http://www.target.com"+white)
url = input (green+"[-]Masukan web target: "+white)
output = input (green+"[-]Masukan nama file output: "+white)

#anim
start = "Maling source code dimulai....\n"
for s in start:
    sys.stdout.write(s)
    sys.stdout.flush()
    time.sleep(0.1)

#parsing
req = requests.get(url, 'html.parser')


#buat file baru
with open(output, "w") as f:
    f.write(req.text)
    f.close()

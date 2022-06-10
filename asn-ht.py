import requests

try :
  pov = input("Enter Your ASN : ")
  bilek = open(pov, 'r').read().splitlines()
  for mk in bilek :
    awikwok = requests.get('https://api.hackertarget.com/aslookup/?q=' + mk)
    
    print("Getting ASN WITH " + mk)
    open('ip.txt', 'a').write(str(awikwok.text) + '\n')
except FileNotFoundError :
  print('File Not Found')


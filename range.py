import ipaddress, sys
import multiprocessing

def anjyme (ip):
  try:
      net4 = ipaddress.ip_network(ip)
      for y in net4.hosts():
        bilek = str(y)
        print("Please Wait")
        open('res.txt','a').write(bilek+'\n')
        
  except FileNotFoundError:
    print('File Not Found')
    print()
    sys.exit(1)

if __name__ == '__main__':
    range = input('LIST IP ? ')
    list_url = open(range, 'r').read().splitlines()
    pool = multiprocessing.Pool(processes=10)
    pool.map(anjyme, list_url)

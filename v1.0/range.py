import requests
import json
import multiprocessing

def fetch(ip):
    try:
        r = requests.get('https://sonar.omnisint.io/reverse/' + ip)
        resp = json.loads(r.text)
        for k, v in resp.items():
            try:
                bilek = requests.get('http://' +str(k), timeout = 3).status_code
                if bilek == '200' :
                    print(bilek + '==> OK')
                    with open('valdi.txt', 'a') as f:
                        f.write(bilek + '\n')
                else : 
                    print('[DIE] {}' .format(k)) 
            except:
                print('[DIE] {}' .format(k))

    except:
        print('Error')

if __name__ == '__main__':
    with open(input('IP Range: '), 'r') as f:
        ips = f.read().splitlines()
    pool = multiprocessing.Pool(processes=10)
    pool.map(fetch, ips)

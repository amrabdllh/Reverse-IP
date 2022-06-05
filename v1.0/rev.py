import requests
import json
import multiprocessing

def fetch(ip):
    try:
        r = requests.get('https://sonar.omnisint.io/reverse/' + ip)
        resp = json.loads(r.text)
        for k, v in resp.items():
            for dns in v:
                print(dns)
                with open('dns.txt', 'a') as f:
                    f.write(dns + '\n')
    except:
        print('Error')

if __name__ == '__main__':
    with open(input('IP Range: '), 'r') as f:
        ips = f.read().splitlines()
    pool = multiprocessing.Pool(processes=10)
    pool.map(fetch, ips)

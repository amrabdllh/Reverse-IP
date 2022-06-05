import asyncio, aiohttp, aiofiles
import json

async def toFile(body):
    ldns = json.loads(body)
    for k, v in ldns.items():
        for dns in v:
            print("DNS : {}".format(dns))
            async with aiofiles.open("good.txt", "a") as f:
                await f.write(dns + "\n")
                await f.close()

async def fetch(session, range_ip):
    api = "https://sonar.omnisint.io/reverse/{}".format(range_ip)
    async with session.get(api) as response:
        resp = await response.text()
        if "error" in resp or "null" in resp:
            pass
        else:
            await asyncio.gather(toFile(resp))

async def fetch_ip_range(session, asn):
    api = "https://api.hackertarget.com/aslookup/?q={}".format(asn)
    async with session.get(api) as response:
        resp = await response.text()
        if "error" in resp:
            return resp.split("\n")
        else:
            return resp.split("\n")

async def main():
    list_bilek = input("Enter ASN: ")
    asen = open(list_bilek, 'r').read().splitlines()
    for asn in asen:
      async with aiohttp.ClientSession() as session:
          list_iprange = await fetch_ip_range(session, asn)
          if "error" in str(list_iprange):
              print("BAD ASN : {}".format(asn))
          else:
              tasks = []
              for iprange in list_iprange:
                  task = asyncio.ensure_future(fetch(session, iprange))
                  tasks.append(task)
              await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(main())
loop.run_until_complete(future)

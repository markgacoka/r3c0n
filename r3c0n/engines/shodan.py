import requests
import json
import os

class Shodan:
    def __init__(self, domain):
        self.domain = domain
        self.subdomain_lst = []

    def sorter(self, subdomains):
        local, final = [], []
        for item in subdomains:
            reversed_sub = ".".join(str(item).split('.')[::-1])
            local.append(reversed_sub)

        sortedlist = sorted(local)
        for item in sortedlist:
            d_reversed_sub = ".".join(str(item).split('.')[::-1])
            final.append(d_reversed_sub)
        return final

    def shodan_script(self, domain):
        subdomains = []
        self.subdomain_lst = []
        SHODAN_API = "UNmOjxeFS2mPA3kmzm1sZwC0XjaTTksy"
        if SHODAN_API == "":
            print("No Riddler API credentials configured")
            return self.subdomain_lst
        else:
            try:
                res = requests.get('https://api.shodan.io/dns/domain/' + domain + '?key=' + SHODAN_API, timeout=10)
                res.raise_for_status()
                data = json.loads(res.text)
                if 'error' in data:
                    self.subdomain_lst = []
                else:
                    for item in data["data"]:
                        entry = item["subdomain"]  
                        record_type = item["type"]
                        value = item["value"]
                        if record_type == 'CNAME' and domain in value: 
                            delim = value.split('.')
                            match = delim[-2] + '.' + delim[-1]
                            if match == domain:
                                subdomains.add(value)

                    for url in self.sorter(subdomains): 
                        self.subdomain_lst.append(url)
            except requests.exceptions.RequestException as err:
                raise Exception("Request Exception:", err)
            except requests.exceptions.HTTPError as errh:
                raise Exception("HTTP Error:", errh)
            except requests.exceptions.ConnectionError as errc:
                raise Exception("Connection Error:", errc)
            except requests.exceptions.Timeout as errt:
                raise Exception("Timeout Error:", errt) 
            else:
                return self.subdomain_lst

    def subdomains(self):
        subdomain_result = self.shodan_script(self.domain)
        return subdomain_result
import requests
from urllib.parse import quote
from r3c0nutils.user_agent import GET_UA

class HackerTarget:
    def __init__(self, domain):
        self.domain = domain
        self.subdomain_lst = []
       
    def hackertarget_script(self, domain):
        url = "https://api.hackertarget.com/hostsearch/?q={0}".format(quote(domain))
        headers = {"user-agent": GET_UA()}
        try:
            res = requests.get(url, headers=headers, timeout=10).text
            hostnames = [result.split(",")[0] for result in res.split("\n")]

            for hostname in hostnames:
                if hostname:
                    self.subdomain_lst.append(hostname)
            return self.subdomain_lst
        except requests.exceptions.RequestException as err:
            print ("Request Exception:", err)
        except requests.exceptions.HTTPError as errh:
            print ("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Connection Error:", errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:", errt) 
        else:
            return self.subdomain_lst

    def subdomains(self):
        subdomain_result = self.hackertarget_script(self.domain)
        return subdomain_result
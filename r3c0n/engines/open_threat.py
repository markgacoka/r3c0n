import json
import requests
from r3c0nutils.formatter import Clean
from r3c0nutils.user_agent import GET_UA

class OpenThreat:
    def __init__(self, domain):
        self.domain = domain
        self.subdomain_lst = []

    def openthreat_script(self, domain):
        self.subdomain_lst = []
        headers = {"User-Agent": GET_UA(), "Content-Type": "application/json"}
        try:
            res = requests.get("https://otx.alienvault.com/otxapi/indicator/hostname/url_list/" + domain, headers=headers, timeout=10)
            res.raise_for_status()
            if res.status_code == 200:
                data = json.loads(res.text)
                for d in data["url_list"]:
                    self.subdomain_lst.append(d["url"])
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
        subdomain_result = self.openthreat_script(self.domain)
        if isinstance(subdomain_result, list) and len(subdomain_result) > 0:
            subdomain_result = Clean(subdomain_result)
            return subdomain_result
        else:
            return []
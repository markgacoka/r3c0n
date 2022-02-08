import json
import requests

class ThreatCrowd:
    def __init__(self, domain):
        self.domain = domain
        self.subdomain_lst = []

    def threatcrowd_script(self, domain):
        try:
            res = requests.get("https://www.threatcrowd.org/searchApi/v2/domain/report/", params={"domain": domain}, timeout=10)
            res.raise_for_status()
            response = json.loads(res.text)
            resp_code = int(response["response_code"])
            if resp_code == 1:
                for sd in response["subdomains"]:
                    self.subdomain_lst.append(sd)
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
        subdomain_result = self.threatcrowd_script(self.domain)
        return subdomain_result
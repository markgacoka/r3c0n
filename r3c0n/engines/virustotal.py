from r3c0nutils.user_agent import GET_UA
import requests

class VirusTotal:
    def __init__(self, domain):
        self.domain = domain
        self.subdomain_lst = []

    def virustotal_script(self, domain):
        VT_API_KEY = ""

        if VT_API_KEY == "":
            print("No VirusTotal API key configured", "red")
            return self.subdomain_lst
        else:
            parameters = {"domain": domain, "apikey": VT_API_KEY}
            headers = {"User-Agent": GET_UA()}
            try:
                res = requests.get("https://www.virustotal.com/vtapi/v2/domain/report", params=parameters, headers=headers, timeout=10)
                res.raise_for_status()
                response_dict = res.json()
                if "subdomains" in response_dict:
                    for sd in response_dict["subdomains"]:
                        self.subdomain_lst.append(sd)
            except requests.exceptions.RequestException as err:
                raise Exception("Request Exception:", err)
            except requests.exceptions.HTTPError as errh:
                raise Exception ("HTTP Error:", errh)
            except requests.exceptions.ConnectionError as errc:
                raise Exception("Connection Error:", errc)
            except requests.exceptions.Timeout as errt:
                raise Exception("Timeout Error:", errt)
            else:
                return self.subdomain_lst

    def subdomains(self):
        subdomain_result = self.virustotal_script(self.domain)
        return subdomain_result
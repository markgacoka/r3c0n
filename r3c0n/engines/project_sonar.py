import requests
from json import loads
from r3c0nutils.user_agent import GET_UA

class ProjectSonar:
    def __init__(self, domain):
        self.domain = domain
        self.subdomain_lst = []

    def filterDomain(self, domain, subdomain_lst):
        domain_parts = domain.split(".")
        filtered = []
        for subdomain in subdomain_lst:
            subdomain_parts = subdomain.split(".")
            if domain_parts == subdomain_parts[-1 * len(domain_parts):]:
                filtered.append(subdomain)

        return filtered

    def projectsonar_script(self, domain):
        url = "http://dns.bufferover.run/dns?q=.{0}".format(domain)
        try:
            headers = {"User-Agent": GET_UA()}
            res = requests.get(url, headers=headers, timeout=10)
            res.raise_for_status()
            response_json = loads(res.text)

            if response_json["FDNS_A"]:
                for record in response_json["FDNS_A"]:
                    self.subdomain_lst += record.split(",")

            if response_json["RDNS"]:
                for record in response_json["RDNS"]:
                    self.subdomain_lst.append(record.split(",")[1])

            self.subdomain_lst = self.filterDomain(domain, set([subdomain.lower() for subdomain in self.subdomain_lst]))
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
        subdomain_result = self.projectsonar_script(self.domain)
        return subdomain_result


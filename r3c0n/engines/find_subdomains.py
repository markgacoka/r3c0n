import requests
from r3c0nutils.user_agent import GET_UA
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class FindSubdomains:
    def __init__(self, domain):
        self.domain = domain
        self.subdomain_lst = []

    def subdomains(self, domain):
        """Returns the list of subdomains from the Anuibis Database.

        Args:
            domain: An inscope domain in which the subdomains are required.
        Returns:
            A list of subdomains extracted from the Anubis database.
        Raises:
            RequestError: Raised on wrong request type.
            HTTPError: Raised on malformed HTTP request.
            ConnectionError: Raised when fails to connect to the server.
            TimeoutError: Raised when request takes too long to come back.
        """
        headers = {"User-Agent": GET_UA()}
        url = "https://findsubdomains.com/subdomains-of/{}".format(domain)
        try:
            res = requests.get(url, headers=headers, verify=False, timeout=10)
            res.raise_for_status()
            name_soup = BeautifulSoup(res.text, "html.parser")
            for link in name_soup.findAll("a", {"class": "aggregated-link"}):
                try:
                    if link.string is not None:
                        self.subdomain_lst.append(link.string.strip())
                except KeyError as errk:
                    return []
            return self.subdomain_lst
        except requests.exceptions.RequestException as err:
            raise ("Request Exception:", err)
        except requests.exceptions.HTTPError as errh:
            raise ("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            raise ("Connection Error:", errc)
        except requests.exceptions.Timeout as errt:
            raise ("Timeout Error:", errt) 
        else:
            return self.subdomain_lst
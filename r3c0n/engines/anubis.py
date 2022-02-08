import requests
from r3c0nutils.user_agent import GET_UA

class Anubis:
    def __init__(self, domain):
        self.domain = domain

    def anubis_script(self, domain):
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
        anubis = []
        headers = {"User-Agent": GET_UA(), "Content-Type": "application/json"}
        try:
            res = requests.get("https://jldc.me/anubis/subdomains/" + domain, headers=headers, timeout=10)
            res.raise_for_status()
            stripped_response = res.text.strip().split(",")
            for id, res in enumerate(stripped_response):
                res = res.replace('"', '')
                if id == 0:
                    res = res[1:]
                if id == len(stripped_response)-1:
                    res = res[:-1]
                anubis.append(res)
            return anubis
        except requests.exceptions.RequestException as err:
            raise ("Request Exception:", err)
        except requests.exceptions.HTTPError as errh:
            raise ("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            raise ("Connection Error:", errc)
        except requests.exceptions.Timeout as errt:
            raise ("Timeout Error:", errt)
        else:
            return anubis

    def subdomains(self):
        subdomain_result = self.anubis_script(self.domain)
        return subdomain_result
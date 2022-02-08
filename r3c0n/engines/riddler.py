import requests
from json import loads
from urllib.parse import quote
from r3c0nutils.user_agent import GET_UA

class Riddler:
    def __init__(self, domain):
        self.domain = domain
        self.subdomain_lst = []

    def riddler_script(self, domain):
        self.subdomain_lst = []
        RIDDLER_USERNAME = ''
        RIDDLER_PASSWORD = ''
        if RIDDLER_USERNAME == "" or RIDDLER_PASSWORD == "":
            print("No Riddler API credentials configured")
            return self.subdomain_lst
        else:
            auth = {"email": RIDDLER_USERNAME, "password": RIDDLER_PASSWORD}
            auth_url = "https://riddler.io/auth/login"
            headers = {"User-Agent": GET_UA()}
            try:
                res = requests.post(auth_url, json=auth, headers=headers, timeout=10)
                res.raise_for_status()
                res_json = loads(res.text)

                if res_json["meta"]["code"] == 200:
                    auth_token = res_json["response"]["user"]["authentication_token"]
                    search = {"query": "pld:{0}".format(quote(domain)), "output": "host"}
                    search_url = "https://riddler.io/api/search"
                    headers = {"User-Agent": GET_UA(), "Content-Type": "application/json", "Authentication-Token": auth_token}
                    search_response = requests.post(search_url, json=search, headers=headers)
                    if search_response.status_code == 200:
                        search_response_json = loads(search_response.text)
                    else:
                        print("An error occurred.")
                        return self.subdomain_lst

                    for item in search_response_json:
                        self.subdomain_lst.append(item["host"])
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
        subdomain_result = self.riddler_script(self.domain)
        return subdomain_result
from anubis import Anubis
from hacker_target import HackerTarget
from open_threat import OpenThreat
from project_sonar import ProjectSonar
from threatcrowd import ThreatCrowd

class All:
    def __init__(self, domain):
        self.domain = domain
        self.subdomain_lst = []

    def subdomains(self):
        subdomain_result = set()        
        subdomain_result = set.union(subdomain_result, set(Anubis(self.domain).subdomains()))
        subdomain_result = set.union(subdomain_result, set(HackerTarget(self.domain).subdomains()))
        subdomain_result = set.union(subdomain_result, set(OpenThreat(self.domain).subdomains()))
        subdomain_result = set.union(subdomain_result, set(ProjectSonar(self.domain).subdomains()))
        subdomain_result = set.union(subdomain_result, set(ThreatCrowd(self.domain).subdomains()))
        return list(subdomain_result)

all = All('coda.io').subdomains()
print(all)
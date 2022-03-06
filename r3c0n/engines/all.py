from r3c0n.engines.anubis import Anubis
from r3c0n.engines.hacker_target import HackerTarget
from r3c0n.engines.open_threat import OpenThreat
from r3c0n.engines.project_sonar import ProjectSonar
from r3c0n.engines.threatcrowd import ThreatCrowd

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
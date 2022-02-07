from scripts.anubis import anubis_script
import yarl

class Clean:
    def cleanup(subdomain_lst: List[str]) -> List[str]:
        """Returns a standardized version of subdomains

        Args:
            subdomain_lst: A list of subdomains from different engines

        Returns:
            A list of correctly formatted subdomains
        """
        clean_lst = []
        for domain in subdomain_lst:
            if domain.strip() == '' or domain == None:
                pass
            if '\n' in domain:
                intermediary = domain.split('\n')
                for i in intermediary:
                    clean_lst.append(i)
            else:
                clean_lst.append(domain)
        for idx, subdomain in enumerate(clean_lst):
            if subdomain.startswith('https://'):
                if yarl.URL(subdomain).path_qs != '' or  yarl.URL(subdomain).path_qs != '/':
                    clean_lst[idx] = str(yarl.URL(subdomain).origin())[8:].strip()
            elif subdomain.startswith('http://'):
                if yarl.URL(subdomain).path_qs != '' or yarl.URL(subdomain).path_qs != '/':
                    clean_lst[idx] = str(yarl.URL(subdomain).origin())[7:].strip()
            else:
                if subdomain.strip() != '' and subdomain != None:
                    subdomain_full = 'http://' + str(subdomain)
                    subdomain_yarl = yarl.URL(subdomain_full)
                    if subdomain_yarl.path_qs != '' or subdomain_yarl.path_qs != '/':
                        clean_lst[idx] = str(subdomain_yarl.origin())[7:].strip()
        return list(filter(None, set(clean_lst)))
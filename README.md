# r3c0n
A tool for performing reconnaissance on web targets in Python

### Description

### Installation
```
pip install r3c0n
```

### Run tests
```
python tests/test_cleanup.py 
```

### Usage
```
from r3c0n import subdomain_scan as scanner

in_scope_domains = ['https://example.com']
subdomains = scanner.all(in_scope_domains)
print(subdomains)

> ['blog.example.com', 'auth.example.com', 'prod-cms.example.com']
```

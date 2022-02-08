# r3c0n
A tool for performing reconnaissance on web targets in Python.

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
```python
from r3c0n.engines import anubis
from r3c0n.engines import hacker_target

domain = 'coda.io'
subdomains = anubis.Anubis(domain).subdomains()
subdomains2 = hacker_target.HackerTarget(domain).subdomains()
print(subdomains)
print(subdomains2)

> 
['www.coda.io', 'dev.coda.io', 'blog.coda.io', 'cdn.coda.io', 'staging.coda.io', 'help.coda.io', 'data.coda.io', 'go.coda.io', 'community.coda.io', 'status.coda.io', 'auth.coda.io', 'bounce.coda.io']

['www.coda.io', 'dev.coda.io', 'blog.coda.io', 'cdn.coda.io', 'staging.coda.io', 'help.coda.io', 'data.coda.io', 'go.coda.io', 'community.coda.io', 'status.coda.io', 'auth.coda.io', 'bounce.coda.io']

```

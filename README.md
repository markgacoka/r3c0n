# r3c0n
A tool for performing reconnaissance on web targets in Python.

### Description
The tool is designed to integrate into your automation workflow for the reconnaissance stage. Given an engine and an in-scope domain, `r3c0n` returns the subdomains and directories associated with the domain.

#### Supported Engines

| Engine      | Importation | API Key |
| ----------- | ----------- | ------- | 
| All engines | from r3c0n.engines.all import All | Free (default) 
| Anubis      | from r3c0n.engine.anubis import Anubis | Free |
| HackerTarget| from r3c0n.engine.hacker_target import HackerTarget | Free |

More examples below at Usage.

### Installation
```
pip install r3c0n
```

### Run tests
```
python tests/test_cleanup.py 
```

### Usage
#### Single import
```python
from r3c0n.engines.anubis import Anubis

domain = 'coda.io'
subdomains = Anubis(domain).subdomains()
print(subdomains)

> ['www.coda.io', 'dev.coda.io', 'blog.coda.io', 'cdn.coda.io', 'staging.coda.io', 'help.coda.io', 'data.coda.io', 'go.coda.io', 'community.coda.io', 'status.coda.io', 'auth.coda.io', 'bounce.coda.io']
```

#### Multiple imports
```python
from r3c0n.engines.anubis import Anubis
from r3c0n.engines.hacker_target import HackerTarget

domain = 'coda.io'

subdomains = set()
subdomains = set.union(subdomains, set(Anubis(domain).subdomains()))
subdomains = set.union(subdomains, set(HackerTarget(domain).subdomains()))
print(list(subdomains))

> ['bounce.coda.io', 'staging.coda.io', 'data.coda.io', 'cdn.coda.io', 'auth.coda.io', 'dev.coda.io', 'adhoc.coda.io', 'go.coda.io', 'coda.io', 'head.coda.io', 'community.coda.io', 'status.coda.io', 'blog.coda.io', 'www.coda.io', 'help.coda.io', 'maze.coda.io']
```

#### Running from the Terminal
```bash
# Prints the subdomains from all the engines on the terminal
r3c0n -d coda.io --engines=all

# Outputs the subdomains found from specific engines to a file
r3c0n -d coda.io --engines=anubis,hackertarget --output subdomains.txt
```

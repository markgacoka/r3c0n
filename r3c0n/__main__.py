import sys
from engines import anubis
import r3c0nutils.viewer as viewer

def main():
    if len(sys.argv) > 1:
        subdomains = anubis.anubis_script(str(sys.argv[1]))
        viewer.show(subdomains)
    else:
        help = 'HELP SECTION'
        viewer.show(help)

if __name__ == "__main__":
    main()
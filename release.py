import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--write',  help='Write new version to version.py', action="store_true")
parser.add_argument('--version',  help='New version')

args = parser.parse_args()

if args.write:
    f = open("simpletestprogram/version.py", "w")
    f.write("# DON'T update with manually, always use release trigger from Github Actions. See RELEASES.md\n")
    f.write("# NON modificare questo file manualmente, use sempre il 'release trigger' da Github Actions. Guarda RELEASES.md\n")
    f.write("__version__ = \'"+args.version+"'\n")
    f.close()
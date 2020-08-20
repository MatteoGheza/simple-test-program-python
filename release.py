import argparse

parser = argparse.ArgumentParser(description="release utils")
parser.add_argument('--write',  help='Write new version to version.py', action="store_true")
parser.add_argument('--version',  help='New version')
parser.add_argument('--artifacts',  help='ZIP dir artifacts', action="store_true")

args = parser.parse_args()

if args.write:
    f = open("simpletestprogram/version.py", "w")
    f.write("# DON'T update with manually, always use release trigger from Github Actions. See RELEASES.md\n")
    f.write("# NON modificare questo file manualmente, use sempre il 'release trigger' da Github Actions. Guarda RELEASES.md\n")
    f.write("__version__ = \'"+args.version+"'\n")
    f.close()
elif args.artifacts:
    import shutil
    shutil.make_archive("build_artifacts/windows-latest", 'zip', "build_artifacts/windows-latest")
    shutil.make_archive("build_artifacts/ubuntu-latest", 'zip', "build_artifacts/ubuntu-latest")
    shutil.make_archive("build_artifacts/macos-latest", 'zip', "build_artifacts/macos-latest")
else:
    print("To release the program, run semantic-release.")
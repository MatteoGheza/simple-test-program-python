if [ "$1" != "--step2" ]; then
    tee simpletestprogram/version.py << END
# DON'T update with manually, always use release trigger from Github Actions. See RELEASES.md
# NON modificare questo file manualmente, use sempre il "release trigger" da Github Actions. Guarda RELEASES.md
END
    echo __version__ = \'${nextRelease.version}\' >> simpletestprogram/version.py
else
    semantic-release
fi
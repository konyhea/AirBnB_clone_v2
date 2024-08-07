#!/usr/bin/python3
'''import necessary packages'''
from fabric.api import env, local, run, lcd, cd
from os import listdir
from os.path import isfile, join

env.hosts = ['18.234.107.69', '54.160.114.105']


def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """
    number = int(number)

    if number == 0:
        number = 1
    # Local cleanup
    archives = sorted([f for f in listdir("versions")
                       if isfile(join("versions", f))])
    archives_to_delete = archives[:-number]
    with lcd("versions"):
        for archive in archives_to_delete:
            local("rm {}".format(archive))
    # Remote cleanup
    for server in env.hosts:
        with cd("/data/web_static/releases"):
            releases = run("ls -tr").split()
            releases_to_delete = [r for r in releases if "web_static_" in r]
            releases_to_delete = releases_to_delete[:-number]
            for release in releases_to_delete:
                run("rm -rf {}".format(release))

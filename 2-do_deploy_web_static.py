#!/usr/bin/python3
'''import packages'''
from fabric.api import env, run, put
from os.path import exists


env.hosts = ['18.234.107.69', '54.160.114.105']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not exists(archive_path):
        return False
    try:
        # Extract the archive file name and the folder name
        archive_file = archive_path.split("/")[-1]
        archive_folder = archive_file.split(".")[0]
        # Upload the archive to /tmp/ directory
        put(archive_path, "/tmp/")
        # Create the target directory
        run("mkdir -p /data/web_static/releases/{}/"
            .format(archive_folder))
        # Uncompress the archive to the target directory
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_file, archive_folder))
        # Remove the archive from the web server
        run("rm /tmp/{}".format(archive_file))
        # Move the files from web_static to the target directory
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(archive_folder, archive_folder))
        # Remove the now empty web_static directory
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_folder))
        # Delete the existing symbolic link
        run("rm -rf /data/web_static/current")
        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(archive_folder))
        return True
    except Exception:
        return False

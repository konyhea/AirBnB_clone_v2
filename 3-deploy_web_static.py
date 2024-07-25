#!/usr/bin/python3
'''import necessary packages'''
from fabric.api import local, env, run, put
from datetime import datetime
from os.path import exists

env.hosts = ['54.160.114.105', '18.234.107.69']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        # Create the versions directory if it doesn't exist
        local("mkdir -p versions")
        # Create the archive name
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = f"versions/web_static_{timestamp}.tgz"
        # Create the archive
        local(f"tar -cvzf {archive_name} web_static")
        # Check if the archive was created successfully and return tpath
        if exists(archive_name):
            return archive_name
        else:
            return None
    except Exception:
        return None


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
        run("mkdir -p /data/web_static/releases/{}/".format(archive_folder))
        # Uncompress the archive to the target directory
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(archive_file, archive_folder))
        # Remove the archive from the web server
        run("rm /tmp/{}".format(archive_file))
        # Move the files from web_static to the target directory
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/"
            .format(archive_folder, archive_folder))
        # Remove the now empty web_static directory
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(archive_folder))
        # Delete the existing symbolic link
        run("rm -rf /data/web_static/current")
        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(archive_folder))
        return True
    except Exception:
        return False


def deploy():
    """
    Creates and distributes an archive to the web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

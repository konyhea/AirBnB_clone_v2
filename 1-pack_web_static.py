#!/usr/bin/python3
'''import packages'''
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        # Create the versions directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")
        # Create the archive name
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = f"versions/web_static_{timestamp}.tgz"
        # Create the archive
        local(f"tar -cvzf {archive_name} web_static")
        # Check if the archive path exists
        if os.path.exists(archive_name):
            return archive_name
        else:
            return None
    except Exception:
        return None

#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import env, local, put, run
import os

env.hosts = ["52.204.69.114", "54.158.80.235"]
env.user = "ubuntu"


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(date)
    if local("tar -cvzf {} web_static".format(archive_path)).succeeded:
        return archive_path
    return None


def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not os.path.exists(archive_path):
        return False

    file_name = archive_path.split("/")[-1]
    base_name = file_name.split(".")[0]
    newest_version = "/data/web_static/releases/" + base_name
    archived_file = "/tmp/" + file_name

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file, newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))
        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False

#!/usr/bin/python3

"""
Deployment 3
"""

from fabric.api import env, put, run, local
from os.path import isdir, exists
import datetime

# Set up Fabric environment
env.hosts = ['52.204.69.114', '54.158.80.235']
env.user = "ubuntu"

# Get the current date and time for versioning
date_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def do_pack():
    """Compress web_static directory into a .tgz archive."""
    try:
        # Create versions directory if it does not exist
        if not isdir('versions'):
            local("mkdir versions")

        # Define the filename for the compressed archive
        filename = "versions/web_static_{}.tgz".format(date_now)

        # Compress the web_static directory
        local('tar -cvzf {} web_static'.format(filename))

        return filename
    except Exception as e:
        print(f"Error during packing: {e}")
        return None


def do_deploy(archive_path):
    """Distribute the archive to the web servers."""
    if not exists(archive_path):
        print("Archive path does not exist")
        return False

    try:
        # Extract file name and create necessary paths
        name_file = archive_path.split("/")[-1]
        no_ext = name_file.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload the archive to the remote server
        put(archive_path, '/tmp/')

        # Create the directory and extract the archive
        run(f'mkdir -p {path}{no_ext}/')
        run(f'tar -xzf /tmp/{name_file} -C {path}{no_ext}/')

        # Clean up temporary files and rearrange directories
        run(f'rm /tmp/{name_file}')
        run(f'mv {path}{no_ext}/web_static/* {path}{no_ext}/')
        run(f'rm -rf {path}{no_ext}/web_static')

        # Update the symbolic link
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {path}{no_ext}/ /data/web_static/current')

        return True
    except Exception as e:
        print(f"Error during deployment: {e}")
        return False


def deploy():
    """Perform the full deployment process."""
    new_filename = do_pack()
    if new_filename is None:
        return False

    return do_deploy(new_filename)

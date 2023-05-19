#!/usr/bin/python3
import os
from fabric.api import run, put
"""
  These modules are used to run the bash commands remotely
"""


env.hosts = ['100.25.143.38', '54.160.96.215']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """
        This function deployes the archive file on both servers and
        unzip them
        Args:
            archive_path (str): path of the archived folder
        Return:
            True on success False on fail
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path ,"/tmp/")
        filename = archive_path.split('/')[-1]
        new_path = '/data/web_static/releases/{}'.format(filename[:-4])
        run("tar -xzvf /tmp/{} -C {}".format(filename, new_path))
        run("rm /tmp/{}".format(filename))
        run("rm -f /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"\
        .format(filename[:-4]))
        return True
    except Exception:
        return False

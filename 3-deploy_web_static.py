#!/usr/bin/python3
import os
from fabric.api import run, env
from file_2 import do_deploy
from file_1 import do_pack
"""
    These modules are used to execute the script
"""


env.hosts = ['100.25.143.38', '54.160.96.215']
env.user = 'ubuntu'
env.key_filename = '/private'


def deploy():
    archive_path = do_pack()
    if not os.path.exists(archive_path):
        return False
    deploy = do_deploy(archive_path)
    return deploy

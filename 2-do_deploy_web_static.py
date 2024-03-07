#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['100.25.19.204', '54.157.159.85']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Deploy web files to server
    """
    try:
        if not (path.exists(archive_path)):
            return False

        # upload archive to server
        put(archive_path, '/tmp/')

        # create target dir
        timestamp = archive_path[-18:-4]
        run(f'sudo mkdir -p /data/web_static/\
            releases/web_static_{timestamp}/')

        # uncompress archive and delete .tgz
        run(f'sudo tar -xzf /tmp/web_static_{timestamp}.tgz -C \
            /data/web_static/releases/web_static_{timestamp}/')

        # remove archive
        run(f'sudo rm /tmp/web_static_{timestamp}.tgz')

        # move contents into host web_static
        run(f'sudo mv /data/web_static/releases/web_static_{timestamp}\
        /web_static/* /data/web_static/releases/web_static_{timestamp}/')

        # remove extraneous web_static dir
        run(f'sudo rm -rf /data/web_static/releases/\
            web_static_{timestamp}/web_static')

        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')

        # re-establish symbolic link
        run(f'sudo ln -s /data/web_static/releases/\
            web_static_{timestamp}/ /data/web_static/current')
    except:
        return False

    # return True
    return True

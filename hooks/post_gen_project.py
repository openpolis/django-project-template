#!/usr/bin/env python
"""Post-generate hook"""

from os import walk, path
from random import choice
from string import Template
import logging

def get_settings_path():
    for (dirpath, dirnames, _) in walk('./project'):
        if 'settings' in dirnames:
            settings_path = path.join(dirpath, 'settings', 'base.py')
            if path.isfile(settings_path):
                return settings_path

def get_env_path():
    for (dirpath, dirnames, _) in walk('./config'):
        if 'samples' in dirnames:
            env_path = path.join(dirpath, 'samples', '.env')
            if path.isfile(env_path):
                return env_path


def generate_secret_key(length=50):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join((choice(chars) for _ in range(length)))


def main():
    """Generate Django SECRET_KEY setting"""
    settings_path = get_settings_path()
    if settings_path:
        logging.debug('patch secret key for settings: %s' % settings_path)
        with open(settings_path) as settings_file:
            tmpl = Template(settings_file.read())
        open(settings_path, 'w').write(tmpl.safe_substitute(secret_key=generate_secret_key()))
    else:
        logging.warning('settings/base.py not found')

    env_path = get_env_path()
    if env_path:
        logging.debug('patch secret key for .env: %s' % env_path)
        with open(env_path) as env_file:
            tmpl = Template(env_file.read())
        open(env_path, 'w').write(tmpl.safe_substitute(secret_key=generate_secret_key()))
    else:
        logging.warning('.env not found')


if __name__ == '__main__':
    main()
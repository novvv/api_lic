#from distutils.core import setup
from setuptools import setup,find_packages
#from setuptools import find_packages
from api_lic.__version__ import __version__
from setuptools.command.install import install
import atexit
from os.path import join, dirname

API_HOME='/opt/denovo/api_lic'

with open('requirements.txt') as f:
    required = f.read().splitlines()

def _post_install():
    import os
    os.system('cp -n {}/.config_files/* {}/'.format(API_HOME, API_HOME))
    #os.system('sudo useradd -d {} webbackend'.format(API_HOME))
    os.system('sudo chown -R webbackend:webbackend {}'.format(API_HOME))


    #os.system('sudo cp /usr/local/lib/python3.5/site-packages/api_lic/etc/supervisor.d/api_lic.ini /etc/supervisor.d/api_lic.ini')
    #os.system('sudo cp /usr/local/lib/python3.5/site-packages/api_lic/etc/ngnix/default.d/api_lic.conf /ngnix/default.d/api_lic.conf')

class new_install(install):
    def __init__(self, *args, **kwargs):
        super(new_install, self).__init__(*args, **kwargs)
        atexit.register(_post_install)

setup(
    name='api_lic',
    version=__version__,
    packages=find_packages(exclude='api_lic_client'),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    url='http://stash.denovolab.com/projects/SMSC/repos/api_engine/browse',
    license='MIT',
    author='valentin novikov',
    author_email='novvvster@gmail.com',
    description='SMSC REST API',
    install_requires=[r for r in required if not 'git+' in r],
    #data_files=[(API_HOME+'schema',['schema.sql','./schema/data.sql'])],
    include_package_data = True,
    data_files=[('./',['requirements.txt','README.md']),
                (API_HOME+'/schema',['schema/schema.sql','schema/data.sql']),
                ('/etc/supervisord.d',['api_lic/etc/supervisord.d/api_lic.ini']),
                ('/etc/nginx/default.d',['api_lic/etc/nginx/default.d/api_lic.conf']),
                (API_HOME+'/.config_files',['api.ini','alembic.ini']),
                (API_HOME+'/files',['.keep'])
                ],
    cmdclass={'install': new_install},
    entry_points={
        'console_scripts': [
            'api_lic_run = api_lic.utils.run:my_gunicorn [gunicorn]',
            'api_lic_worker = api_lic.utils.run:my_worker [celery]',
            'api_lic_beat = api_lic.utils.run:my_beat     [celery]',
        ]
    },
    extras_require={
        'gevent':  ["gevent==1.2.2"],
        'celery':  ["celery>=4.1.0","billiard>=3.5.0.3"],
        'gunicorn': ["gunicorn>=19.7.1"],

    },
    dependency_links=[
        "git+ssh://git@stash.denovolab.com:7999/af/falcon_rest.git",
        "git+https://github.com/dpallot/simple-websocket-server.git"
    ]
)



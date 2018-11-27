import sys
import contextlib

from gunicorn.app.wsgiapp import run as grun
from celery.__main__ import main as celery

@contextlib.contextmanager
def redirect_argv(args):
    sys._argv = sys.argv[:]
    sys.argv=[sys._argv[0]]+args
    yield
    sys.argv = sys._argv

def my_gunicorn():
    args='api_lic.wsgi:app -b localhost:8012 -t 600 -w 4 --reload'.split(' ')
    with redirect_argv(args):
        grun()

def my_worker():
    if len(sys.argv) < 2:
        print('usage:\n {} [NAME]'.format(sys.argv[0]))
        print('NAME is worker name')
        return
    name=sys.argv[1]
    #args = '-q -b redis://localhost:6379/0 -E -A api_lic.task worker -l debug -n worker.{} -P gevent'.format(name).split(' ')
    args = '-q -b redis://localhost:6379/0 -E -A api_lic.task worker -l debug -n worker.{}'.format(name).split(' ')
    with redirect_argv(args):
        celery()

def my_beat():
    args = '-q -b redis://localhost:6379/0 -A api_lic.task beat -l debug'.split(' ')
    with redirect_argv(args):
        celery()

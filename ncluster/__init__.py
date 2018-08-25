import os
import collections

from . import aws_backend
from . import aws_util
from . import local_backend
from . import backend # TODO: remove?


def set_backend(backend_name):
  """Sets backend (local or aws)"""
  global _backend
  if backend_name == 'aws':
    _backend = aws_backend
  elif backend_name == 'local':
    _backend = local_backend
  else:
    assert False, f"Unknown backend {backend_name}"


def make_run(name='', **kwargs):
  return _backend.Run(name, **kwargs)


def make_job(name='', **kwargs):
  return _backend.make_job(name, **kwargs)


def make_task(name='', **kwargs):
  return _backend.make_task(name, **kwargs)


def join(things_to_join):
  if isinstance(things_to_join, collections.Iterable):
    for thing in things_to_join:
      thing.join()
  else:
    things_to_join.join()


# set default backend from environment
if 'NCLUSTER_BACKEND' in os.environ:
  set_backend(os.environ['NCLUSTER_BACKEND'])
else:
  set_backend('aws')
  

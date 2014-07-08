import os
from libs import oauth

DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Devel')

def get_host():
  return "http://" + os.environ['SERVER_NAME'] + ((':' + os.environ['SERVER_PORT']) if os.environ['SERVER_PORT'] != '80' else '')

SECURE_COOKIE = 'SAHA249FJFK39T6JGN49549TRHGJ549TFJTR8'

OAUTH_CALLBACK_URL = '%s/%s' % (get_host(), 'oauth/verify')
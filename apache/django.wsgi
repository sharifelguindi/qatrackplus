import os, sys

sys.path.append('c:/deploy/qatrackplus')
sys.path.append('c:/deploy/qatrackplus/qatrack')
os.environ['DJANGO_SETTINGS_MODULE'] = 'qatrack.settings'


# Activate your virtual env
activate_env="c:/deploy/venvs/qatrack/Scripts/activate_this.py"
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
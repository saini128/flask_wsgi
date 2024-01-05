# application.wsgi
import sys
sys.path.insert(0, '/var/www/flaskapp')

from application import app as application

# application.wsgi
import sys
sys.path.insert(0, '/var/www/flask_wsgi')

from application import app as application

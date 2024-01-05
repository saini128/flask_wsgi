# application.wsgi
import sys
sys.path.insert(0, '/var/www/flask_wsgi')


activate_this='/home/singh/.local/share/virtualenvs/flask_wsgi-VIdC3nvo/bin/activate_this.py'
with open (activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from application import app as application

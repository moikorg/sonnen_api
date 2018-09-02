"""
this is the "secret sauce" -- a single entry-point that resolves the
import dependencies.  If you're using blueprints, you can import your
blueprints here too.

then when you want to run your app, you point to main.py or `main.app`

==> Inspired by: http://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/
"""

from app import app, db
import api
import models
import views
import logging


# set the logging level to ERROR to reduce the verbosity in the shell
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

#admin.setup()
#api.setup()


if __name__ == '__main__':
    views.app.run(debug=False)
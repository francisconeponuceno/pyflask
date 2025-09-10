# pip install flask-debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
# pip install flask-qtf
from flask_wtf import CSRFProtect

toolbar = DebugToolbarExtension()
csrf = CSRFProtect()
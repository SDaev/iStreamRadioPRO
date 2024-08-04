from waitress import serve
from app import *

serve(app, listen="*:80")

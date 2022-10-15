from flask import Flask

app = Flask(__name__)

import hmf.controllers.home
import hmf.controllers.saludo
#!flask/bin/python
import os
from app import app

#app.run(debug = True)
port = int(os.getenv("PORT"))
app.run(host='0.0.0.0', port=port)
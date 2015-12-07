import requests
import sys

# file called credentials.py which constains the following vars
from credentials import *

# PARTICLE_ID="YOUR_PARTICLE_ID"
# PARTICLE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
# PARTICLE_FUNCTION = "YOUR_PARTICLE_FUNCTION"


def sendToPhoton(PARTICLE_FUNCTION):
    # VARIABLES
    if (PARTICLE_FUNCTION == ""):
        PARTICLE_FUNCTION = "LED"
    URL = "https://api.particle.io/v1/devices/"
    SLASH = "/"
    TOKEN_LABEL = "?access_token="
    PAYLOAD = {"args": "on"}

    # COMMANDLINE ARGS
    # 0 -  file_name.py , 1 - arg[0] ...
    if (len(sys.argv) > 1):
        PAYLOAD = {"args": sys.argv[1]}

    # MAGIC
    print "Dancing monkeys are executing your request..."
    result = requests.post(URL + PARTICLE_ID + SLASH +
                           PARTICLE_FUNCTION + TOKEN_LABEL +
                           PARTICLE_ACCESS_TOKEN, json=PAYLOAD)
    return None
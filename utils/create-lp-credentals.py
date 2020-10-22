# pip3 install launchpadlib
# https://help.launchpad.net/API/launchpadlib
# https://help.launchpad.net/API/SigningRequests

import os
import sys
import argparse

from launchpadlib.launchpad import Launchpad
from launchpadlib.launchpad import Credentials

home = os.getenv("HOME")
workdir = home+"/snap-builds"
cachedir = workdir+"/tmp"
creds = "./credentials"

launchpad = Launchpad.login_with('EdgeX Snap Build Trigger',
                                 'production', cachedir,
                                 credentials_file=creds,
                                version='devel')

print ("The secrets are in the ./credentials file")
print("Copy them to the Github Secrets LP_CONSUMER_NAME, LP_ACCESS_TOKEN and LP_ACCESS_SECRET")
edgex_team = launchpad.people["canonical-edgex"]
print(edgex_team.display_name)


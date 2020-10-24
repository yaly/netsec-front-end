#!/usr/bin/env python
# Author: alymy@mail.uc.edu
import os
import subprocess

# Pull latest, remove old container and image, build new image, run new container
os.system('sudo git reset --hard HEAD')

os.system('sudo git clean -f -d')

os.system('sudo git pull')

os.system('sudo cp /opt/config-repository/front-end/services.json ./services.json')

os.system('sudo cp /opt/config-repository/front-dash/config.json ./config.json')

os.system('sudo docker kill front-end')

os.system('sudo docker rm front-end')

os.system('sudo docker rmi front-end')

os.system('sudo docker build . -t front-end')

os.system('sudo docker run -itd --name front-end -p 0.0.0.0:8000:80 front-end')

os.system('sleep 3')

# Quick service check
print("Health Check: Testing URL end-point...")

(response, error) = subprocess.Popen(['curl', '-s', 'http://localhost:8000/front-end'], stdout=subprocess.PIPE).communicate()
if 'Service is running' not in response:
    print('Health Check FAILED: Front end response was invalid')
    exit()

print("Health Check: SUCCESS")

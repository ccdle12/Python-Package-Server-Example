import os
import time

os.system('docker-compose down')
os.system('docker-compose up -d pypi_project')
time.sleep(5)

os.system('docker-compose up -d project_a project_b')

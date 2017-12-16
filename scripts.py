import os
import sys

def build_containers():
    os.system("docker build -t alc-mongo ./Mongo")
    os.system("docker build -t alc-app ./App")

def start_containers():
    os.system("docker run --name alc-mongo-container -d -p 27017:27017 alc-mongo")
    os.system("docker run --name alc-app-container -d --network='host' alc-app")
    print("MongoDB running on port 27017")
    print("App running on port 3000")

def stop_containers():
    print("Stopping containers")
    os.system("docker container stop alc-mongo-container alc-app-container")
    os.system("docker container rm alc-mongo-container alc-app-container")  

if __name__ == '__main__':    
    if "--build" in sys.argv:
        build_containers()
    if "--run" in sys.argv:
        start_containers()
    elif "--stop" in sys.argv:
        stop_containers()
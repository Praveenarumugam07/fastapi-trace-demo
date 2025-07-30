from fastapi import FastAPI
from otel_config import init_tracer
import time

app = FastAPI()
init_tracer(service_name="sample-api")

@app.get("/")
def read_root():
    time.sleep(0.2)
    return {"message": "Hello World"}

@app.get("/build-stage")
def simulate_build():
    time.sleep(0.5)
    return {"stage": "Build Completed"}

@app.get("/test-stage")
def simulate_test():
    time.sleep(0.3)
    return {"stage": "Tests Passed"}

@app.get("/deploy-stage")
def simulate_deploy():
    time.sleep(0.6)
    return {"stage": "Deployed Successfully"}

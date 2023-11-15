import psutil # Needed to get CPU and Memory usage information
from flask import Flask, render_template # Flask needed to create app, render_template needed to create metrics graph

# Creation of App
app = Flask(__name__)

@app.route("/") # App will run on home folder

def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    Message = None
    
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')
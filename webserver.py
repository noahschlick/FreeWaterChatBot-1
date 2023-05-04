from flask import Flask
from threading import Thread

app = Flask("")

#UptimeRobot will ping this directory to keep bot alive
@app.route("/")
def home():
  return "Im Alive"

def run():
  app.run(host="0.0.0.0", port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
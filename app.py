from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello from Azure App Service</h1><p>Deployed via GitHub Actions</p>"

if __name__ == "__main__":
    app.run()

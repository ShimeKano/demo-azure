from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Azure Cloud Demo</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #0078D4, #00BCF2);
            font-family: 'Segoe UI', Tahoma, sans-serif;
            color: white;
        }
        .card {
            background: rgba(255,255,255,0.15);
            padding: 40px;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.25);
            max-width: 420px;
        }
        h1 {
            margin-bottom: 10px;
            font-size: 32px;
        }
        p {
            font-size: 16px;
            opacity: 0.9;
        }
        .badge {
            margin-top: 20px;
            display: inline-block;
            padding: 8px 16px;
            border-radius: 999px;
            background: white;
            color: #0078D4;
            font-weight: 600;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Hello from Azure ☁️</h1>
        <p>Cloud Provider: Microsoft Azure</p>
        <p>Service: App Service (PaaS)</p>
        <p>Runtime: Python 3.10</p>
        <p>Time: {{ time }}</p>
        <div class="badge">Deployed via GitHub Actions</div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, time=datetime.now())

if __name__ == "__main__":
    app.run()

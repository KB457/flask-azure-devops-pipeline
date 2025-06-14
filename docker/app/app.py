from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Welcome to My DevOps Project</title>
            <style>
                body {
                    background-color: #f0f4f8;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 100px;
                }
                h1 {
                    color: #2b6cb0;
                    font-size: 3em;
                }
                p {
                    font-size: 1.2em;
                    color: #555;
                }
            </style>
        </head>
        <body>
            <h1>🚀 Hello from Flask on Azure!</h1>
            <p>This app is part of my CI/CD DevOps pipeline using Terraform, Docker & GitHub Actions.</p>
        </body>
    </html>
    '''

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


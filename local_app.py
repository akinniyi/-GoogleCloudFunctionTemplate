from flask import Flask, request
from main import main
app = Flask(__name__)

# Create a local "app" for generating request contexts for local development.
def index():
    return main(request)

if __name__ == '__main__':
    app.run(debug=True)

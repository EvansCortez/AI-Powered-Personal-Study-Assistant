from flask import Flask, request, jsonify
from routes.upload import upload_bp

app = Flask(__name__)
app.register_blueprint(upload_bp, url_prefix="/upload")

if __name__ == "__main__":
    app.run(debug=True)

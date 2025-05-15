from flask import Blueprint, request, jsonify
from services.nlp_service import extract_topics_from_pdf

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    topics = extract_topics_from_pdf(file)
    return jsonify({"topics": topics})

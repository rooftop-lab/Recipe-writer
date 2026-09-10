import os
import sys
import io

# Ensure current directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request, send_file
from generate_pdf import create_recipe_pdf

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    url = request.form.get("url", "")
    language = request.form.get("language", "ta")
    instructions = request.form.get("instructions", "")

    pdf_buffer = io.BytesIO()
    create_recipe_pdf(pdf_buffer, video_url=url, language=language, custom_instructions=instructions)
    pdf_buffer.seek(0)

    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name="Bilingual_Recipe_Sheet.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

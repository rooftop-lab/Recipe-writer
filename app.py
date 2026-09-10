import os
from flask import Flask, render_template, request, send_file, Response
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

    output_pdf = "travel_premix_recipes_bilingual.pdf"
    if not os.path.exists(output_pdf):
        create_recipe_pdf(output_pdf)

    return send_file(
        output_pdf,
        as_attachment=True,
        download_name="Bilingual_Recipe_Sheet.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

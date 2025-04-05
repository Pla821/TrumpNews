
from flask import Flask, render_template, send_file
import json, csv, os

app = Flask(__name__)

def load_data():
    with open("country_impact.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map")
def map_page():
    return render_template("map.html")

@app.route("/export")
def export_page():
    return render_template("export.html")

@app.route("/export/csv")
def export_csv():
    data = load_data()
    filename = "impact_export.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Country", "Time", "Source", "Title"])
        for country, records in data.items():
            for r in records:
                writer.writerow([country, r["time"], r["source"], r["title"]])
    return send_file(filename, as_attachment=True)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/admin")
def admin_page():
    return render_template("admin.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

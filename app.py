from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse', methods=['POST'])
def analyse():
    pair = request.form.get('pair')
    timeframe = request.form.get('timeframe')
    screenshot = request.files.get('screenshot')

    if screenshot:
        filename = screenshot.filename
        filepath = os.path.join("static", filename)
        os.makedirs("static", exist_ok=True)
        screenshot.save(filepath)
        # Mocked response (in real case: analyse with AI)
        return jsonify({
            "pair": pair,
            "timeframe": timeframe,
            "result": f"✔️ Analyse détectée pour {pair} sur {timeframe} avec OB + FVG + Sweep."
        })
    return jsonify({"error": "No screenshot received"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=10000)
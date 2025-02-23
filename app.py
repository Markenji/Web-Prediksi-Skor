from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('model_regresi_linear.pkl')

@app.route('/')
def index():
    return render_template('index.html')  # Flask akan mencari index.html di folder 'templates'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        jam_belajar = float(request.form['jam_belajar'])
        prediksi_skor = model.predict(np.array([[jam_belajar]]))[0]
        return jsonify({'skor': round(prediksi_skor, 2)})
    except ValueError:
        return jsonify({'error': 'Input jam belajar tidak valid'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
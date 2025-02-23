# Prediksi Skor Siswa Berbasis Jam Belajar

Aplikasi web sederhana untuk memprediksi skor siswa berdasarkan jam belajar menggunakan model regresi linear.

## Deskripsi

Proyek ini mengimplementasikan sistem prediksi skor siswa berbasis web. Pengguna dapat memasukkan jumlah jam belajar, dan sistem akan memprediksi skor siswa berdasarkan model regresi linear yang telah dilatih. Proyek ini terdiri dari dua bagian utama:

1.  **Backend (Flask):** Bertanggung jawab untuk menerima input jam belajar, menjalankan model regresi linear, dan mengembalikan prediksi skor.
2.  **Frontend (HTML, JavaScript):** Menyediakan antarmuka interaktif bagi pengguna untuk memasukkan jam belajar dan melihat hasil prediksi.

Model regresi linear dilatih menggunakan data jam belajar dan skor siswa. Library `joblib` digunakan untuk menyimpan dan memuat model.

## Cara Penggunaan

1.  **Clone Repositori:**
    ```bash
    git clone [https://github.com/nama-pengguna/Prediksi-Skor-Siswa.git](https://github.com/nama-pengguna/Prediksi-Skor-Siswa.git)  # Ganti dengan nama pengguna dan repositori Anda
    ```

2.  **Instal Dependensi:**
    ```bash
    pip install -r requirements.txt  # Jika Anda memiliki file requirements.txt
    # Atau instal satu per satu:
    pip install Flask numpy joblib scikit-learn
    ```

3.  **Jalankan Aplikasi:**
    ```bash
    python app.py
    ```

4.  **Buka Aplikasi:**
    Buka browser dan akses `http://127.0.0.1:5000` untuk melihat aplikasi web.

## Struktur Proyek

Prediksi-Skor-Siswa/
├── app.py              # Backend Flask
├── templates/
│   └── index.html      # Frontend HTML
├── model_regresi_linear.pkl  # Model regresi linear yang telah dilatih
└── requirements.txt   # Daftar dependensi (opsional)


## Data

Data yang digunakan untuk melatih model (opsional):

*   Anda dapat menjelaskan secara singkat data yang Anda gunakan untuk melatih model.
*   Jika Anda menggunakan dataset publik, sertakan tautan ke dataset tersebut.
*   Jika Anda memiliki file data (misalnya, CSV), jelaskan format dan fitur-fiturnya.

## Model

Model regresi linear disimpan dalam file `model_regresi_linear.pkl`. Model ini dilatih menggunakan library `scikit-learn`.

## Cara Melatih Model (Opsional)

Jika Anda ingin memberikan informasi tentang bagaimana model dilatih, Anda dapat menambahkan bagian ini. Misalnya:

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# ... (kode untuk memuat atau membuat data) ...

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, 'model_regresi_linear.pkl')

Kontributor
Adha Ozy Prima Dewangga (https://github.com/markenji)

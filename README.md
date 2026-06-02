# Scanora Dashboard

Scanora Dashboard adalah dashboard analisis data berbasis **Streamlit** yang dikembangkan untuk mendukung proyek capstone Scanora. Dashboard ini digunakan untuk mengeksplorasi dan memvisualisasikan **fruits image dataset** serta **fruits consumption dataset**, sehingga insight utama terkait distribusi data buah, kondisi kesegaran, kombinasi kelas, dan pola konsumsi buah dapat dipahami secara lebih interaktif.

## Dashboard Overview

Dashboard ini membantu menampilkan hasil eksplorasi data dari dua konteks utama:

1. **Fruits Image Dataset**
   Digunakan untuk melihat distribusi data gambar berdasarkan jenis buah, kondisi kesegaran, kombinasi kelas, serta preview gambar.

2. **Fruits Consumption Dataset**
   Digunakan untuk melihat posisi konsumsi buah target Scanora, yaitu apel, pisang, dan jeruk, dibandingkan komoditas buah lainnya.

## Main Features

Dashboard menampilkan beberapa fitur utama:

* **Overview Dataset**
  Menampilkan ringkasan jumlah gambar, jenis buah, kondisi buah, kombinasi kelas, serta ringkasan konsumsi buah target.

* **Fruits Image Dataset Analysis**
  Menampilkan visualisasi distribusi jenis buah, distribusi kondisi kesegaran, kombinasi kelas, heatmap, dan sample image preview.

* **Fruits Consumption Dataset Analysis**
  Menampilkan rata-rata konsumsi buah target Scanora dan top komoditas buah berdasarkan rata-rata konsumsi.

* **Interactive Filter**
  Pengguna dapat memilih jenis buah, kondisi buah, dan jumlah komoditas konsumsi teratas yang ingin ditampilkan.

* **Key Insights**
  Menampilkan rangkuman insight utama dari hasil analisis data gambar dan data konsumsi buah.

## Dataset Used

Repository ini menggunakan file hasil olahan dari proses Data Science:

```bash
fruit_consumption_summary.csv
metadata_processed.csv
```

Keterangan:

* `metadata_processed.csv` berisi metadata final fruits image dataset setelah proses cleaning dan preprocessing.
* `fruit_consumption_summary.csv` berisi ringkasan data konsumsi buah setelah proses cleaning, feature engineering, dan analisis konsumsi.

Dataset gambar mentah tidak disertakan dalam repository karena ukuran file cukup besar. Proses lengkap data gathering, assessing, cleaning, feature engineering, EDA, dan preprocessing tersedia pada repository Data Science utama.

## Project Structure

Struktur repository dashboard:

```bash
scanora-dashboard/
├── dashboard/
│   ├── image/
│   └── streamlit_app.py
├── fruit_consumption_summary.csv
├── metadata_processed.csv
├── requirements.txt
├── .gitignore
└── README.md
```

Keterangan:

* `dashboard/streamlit_app.py` merupakan file utama aplikasi Streamlit.
* `dashboard/image/` berisi asset gambar yang digunakan pada dashboard.
* `fruit_consumption_summary.csv` berisi data konsumsi buah hasil olahan.
* `metadata_processed.csv` berisi metadata final dataset gambar buah.
* `requirements.txt` berisi daftar dependencies untuk menjalankan dashboard.

## Live Dashboard

Dashboard dapat diakses melalui link berikut:

```text
https://scanora-dashboard-capstone-project.streamlit.app
```

## How to Run Locally

Ikuti langkah berikut untuk menjalankan dashboard secara lokal.

### 1. Clone Repository

```bash
git clone https://github.com/emilianaaelgaa/scanora-dashboard.git
cd scanora-dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit App

```bash
streamlit run dashboard/streamlit_app.py
```

Setelah dijalankan, dashboard dapat diakses melalui browser pada alamat lokal yang ditampilkan oleh Streamlit, misalnya:

```text
http://localhost:8501
```

## Related Repository

Repository Data Science utama tersedia pada link berikut:

```text
https://github.com/ameliavega932-star/Scanora-DS
```

Repository tersebut berisi notebook utama, workflow Data Science, output metadata, laporan teknis, serta dokumentasi proses data dari awal hingga akhir.

## Tech Stack

Dashboard ini dikembangkan menggunakan:

* Python
* Streamlit
* Pandas
* Matplotlib / Plotly
* PIL
* NumPy

## Notes

Dashboard ini berfungsi sebagai media eksplorasi dan visualisasi hasil analisis data. Dashboard tidak digunakan sebagai aplikasi utama untuk pengguna akhir, melainkan sebagai pendukung proses Data Science dalam proyek Scanora.

Untuk menjalankan dashboard dengan benar, pastikan file `metadata_processed.csv` dan `fruit_consumption_summary.csv` tersedia pada root repository sesuai struktur folder yang digunakan.

# Dasbor Berbagi Sepeda

Proyek ini adalah dasbor untuk memvisualisasikan data berbagi sepeda. Proyek ini menggunakan `Streamlit` untuk antarmuka web dan menyediakan visualisasi interaktif penggunaan sepeda berdasarkan berbagai faktor seperti cuaca, musim, dan lainnya.

git add README.md dashboard/dashboard.py data/all_data_bike.csv url.txt

## Fitur

- Visualisasikan penggunaan sepeda berdasarkan tanggal
- Analisis penggunaan sepeda berdasarkan kondisi cuaca
- Analisis penggunaan sepeda di berbagai musim
- Filter data berdasarkan rentang tanggal
- Tampilkan metrik seperti total dan rata-rata penggunaan sepeda harian

## Persyaratan

- Python 3.x
- `pandas`, `matplotlib`, `seaborn`, `streamlit` (lihat `requirements.txt`)

## Petunjuk Penyiapan

1. **Klon repositori:**
```bash
git clone <your-repository-url>
```

2. **Navigasi ke direktori proyek:**
```bash
cd submission
```

3. **Instal dependensi yang diperlukan:**
```bash
pip install -r requirements.txt
```

4. **Jalankan dasbor Streamlit:**
```bash
streamlit run dashboard.py
```

## Penggunaan

Setelah menjalankan Aplikasi Streamlit akan membuka tab baru di peramban web tempat Anda dapat menjelajahi dasbor. Gunakan bilah sisi untuk memilih rentang tanggal dan berinteraksi dengan berbagai visualisasi.

## Struktur File

- `dashboard.py`: Skrip utama untuk menjalankan dasbor Streamlit.
- data/: Berisi kumpulan data (all_data_bike.csv) yang digunakan untuk visualisasi.
- requirements.txt: Mencantumkan semua pustaka Python yang diperlukan untuk menjalankan proyek.
- README.md: Petunjuk untuk menyiapkan dan menjalankan proyek.

## Kumpulan data

Kumpulan data berisi data penggunaan sepeda, termasuk:
- Tanggal (dteday)
- Musim (season)
- Cuaca (weathersit_x)
- Suhu (temp_x)
- Jumlah penggunaan sepeda (cnt_x)
- ...dan banyak lagi.

Data digunakan untuk menghasilkan berbagai visualisasi di dasbor.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat berkas LICENSE untuk detailnya.
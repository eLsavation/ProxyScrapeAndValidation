# Proxy Scrape & Validation Tool 🚀

## 📜 Deskripsi
Sebuah skrip Python untuk mengambil proxy dari API yang tercantum dalam file `api.txt`, menyimpannya dalam file `get-proxy.txt`, dan memvalidasi proxy tersebut. Proxy yang valid akan disimpan di `valid-proxy.txt`. Skrip ini dilengkapi dengan output yang menarik, menggunakan warna dan simbol untuk menambah estetika.

## 🛠️ Fitur
- **Ambil Proxy**: Mengambil proxy dari API yang terdaftar di file `api.txt`.
- **Validasi Proxy**: Memeriksa apakah proxy dapat digunakan.
- **Output Berwarna**: Menampilkan status proxy (valid/invalid) dengan warna dan simbol.
- **Simpan Hasil**: Proxy mentah disimpan di `get-proxy.txt`, proxy valid disimpan di `valid-proxy.txt`.

## 🔧 Instalasi
1. Clone repositori ini:
   ```bash
   git clone https://github.com/elsavation/ProxyScrapeAndValidation.git
   cd ProxyScrapeAndValidation
   ```
2. Install dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Cara Menggunakan
1. Tambahkan API proxy Anda ke dalam file `api.txt`, satu API per baris:
   ```
   https://api1.com/proxies
   https://api2.com/proxies
   ```
2. Jalankan skrip:
   ```bash
   python proxy-scrape-test.py
   ```
3. Hasil:
   - **Proxy mentah** disimpan di `get-proxy.txt`.
   - **Proxy valid** disimpan di `valid-proxy.txt`.

## 💂‍♂️ Struktur Proyek
```
.
├── api.txt             # File berisi URL API proxy
├── get-proxy.txt       # File hasil proxy mentah
├── valid-proxy.txt     # File hasil proxy valid
├── proxy-scrape-test.py # Skrip utama
├── requirements.txt    # File dependensi
```

## 📘 Contoh Output
```
   _____                        _____                                     __      __   _ _     _       _   _
  |  __ \                      / ____|                             ___    \ \    / /  | (_)   | |     | | (_)
  | |__) | __ _____  ___   _  | (___   ___ _ __ __ _ _ __   ___   ( _ )    \ \  / /_ _| |_  __| | __ _| |_ _  ___  _ __
  |  ___/ '__/ _ \ \/ / | | |  \___ \ / __| '__/ _` | '_ \ / _ \  / _ \/\   \ \/ / _` | | |/ _` |/ _` | __| |/ _ \| '_ \
  | |   | | | (_) >  <| |_| |  ____) | (__| | | (_| | |_) |  __/ | (_>  <    \  / (_| | | | (_| | (_| | |_| | (_) | | | |
  |_|   |_|  \___/_/\_\\__, | |_____/ \___|_|  \__,_| .__/ \___|  \___/\/     \/ \__,_|_|_|\__,_|\__,_|\__|_|\___/|_| |_|
                        __/ |                       | |
                       |___/                        |_|
  Made with love by eLsavation

[✔] Proxy diambil dari: https://api1.com/proxies
[✔] Proxy diambil dari: https://api2.com/proxies
[✔] Proxy mentah berhasil disimpan ke get-proxy.txt

[🔍] Menguji proxy...
[✔] Proxy valid: 123.123.123.123:8080
[✘] Proxy invalid: 124.124.124.124:8080
[✔] Proxy yang valid disimpan ke valid-proxy.txt
```

## 💡 Catatan
- Pastikan API yang digunakan memberikan daftar proxy dalam format teks.
- Proxy diuji dengan waktu batas (`timeout`) 5 detik untuk efisiensi.

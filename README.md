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

[*] Proxy diambil dari: https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&country=id,sg&protocol=http&proxy_format=protocolipport&format=text&timeout=1618
[INFO] Proxy mentah berhasil disimpan ke get-proxy.txt
[START] Proxy Validation Starting...
[HTTP] Proxy valid: 119.8.182.222:3128
[HTTP] Proxy valid: 8.219.102.193:2000
[HTTP] Proxy valid: 5.223.41.232:7000
[HTTP] Proxy invalid: 103.224.124.93:8080
[HTTP] Proxy valid: 157.20.209.105:8080
[HTTP] Proxy valid: 103.151.140.124:10609
[HTTP] Proxy valid: 143.42.66.91:80
[HTTP] Proxy invalid: 116.254.96.111:8080
[HTTP] Proxy valid: 103.234.35.142:8090
[HTTP] Proxy valid: 178.128.113.118:23128
[HTTP] Proxy invalid: 103.176.96.217:8082
[INFO] Proxy yang valid disimpan ke valid-proxy.txt

```

## 💡 Catatan
- Pastikan API yang digunakan memberikan daftar proxy dalam format teks.

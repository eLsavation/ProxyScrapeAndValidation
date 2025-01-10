import requests
from termcolor import colored
import time
from urllib.parse import urlparse
from requests.auth import HTTPProxyAuth
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def print_banner():
    banner = r"""
   _____                        _____                                     __      __   _ _     _       _   _
  |  __ \                      / ____|                             ___    \ \    / /  | (_)   | |     | | (_)
  | |__) | __ _____  ___   _  | (___   ___ _ __ __ _ _ __   ___   ( _ )    \ \  / /_ _| |_  __| | __ _| |_ _  ___  _ __
  |  ___/ '__/ _ \ \/ / | | |  \___ \ / __| '__/ _` | '_ \ / _ \  / _ \/\   \ \/ / _` | | |/ _` |/ _` | __| |/ _ \| '_ \
  | |   | | | (_) >  <| |_| |  ____) | (__| | | (_| | |_) |  __/ | (_>  <    \  / (_| | | | (_| | (_| | |_| | (_) | | | |
  |_|   |_|  \___/_/\_\\__, | |_____/ \___|_|  \__,_| .__/ \___|  \___/\/     \/ \__,_|_|_|\__,_|\__,_|\__|_|\___/|_| |_|
                        __/ |                       | |
                       |___/                        |_|
  Made with love by eLsavation
      """
    print(colored(banner, "cyan"))

def test_proxy(proxy, username=None, password=None):
    """
    Menguji apakah proxy berfungsi dengan autentikasi (jika ada).
    :param proxy: Proxy yang akan diuji (format: ip:port)
    :param username: Username untuk autentikasi (jika ada)
    :param password: Password untuk autentikasi (jika ada)
    :return: True jika proxy berfungsi, False jika tidak
    """
    test_url = "http://httpbin.org/ip"  # URL untuk pengujian proxy
    
    # Mengurai proxy URL jika ada autentikasi dalam URL
    parsed_proxy = urlparse(proxy)
    
    if parsed_proxy.username and parsed_proxy.password:
        # Menggunakan username dan password dari URL
        auth = HTTPProxyAuth(parsed_proxy.username, parsed_proxy.password)
        proxy_url = f"{parsed_proxy.hostname}:{parsed_proxy.port}"  # Menghindari 'http://' yang salah
        protocol = parsed_proxy.scheme.upper()  # Menentukan protokol yang digunakan
    else:
        # Jika tidak ada autentikasi, menggunakan parameter yang diberikan
        auth = HTTPProxyAuth(username, password) if username and password else None
        proxy_url = proxy
        protocol = "HTTP"  # Default protokol

    proxies = {
        "http": f"http://{proxy_url}",
        "https": f"https://{proxy_url}"
    }

    try:
        session = requests.Session()
        retry = Retry(total=2, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        response = session.get(test_url, proxies=proxies, auth=auth, timeout=5)  # Timeout diperpendek
        
        if response.status_code == 200:
            print(colored(f"[{protocol}] Proxy valid: {proxy}", "green"))
            return True, protocol
    except requests.exceptions.RequestException:
        # Menampilkan pesan singkat saat error terjadi
        print(colored(f"[{protocol}] Proxy invalid: {proxy}", "red"))
    return False, protocol

def get_proxies(api_file, output_file):
    """
    Mengambil proxy dari API yang terdaftar di file dan menyimpannya ke dalam file.
    :param api_file: File yang berisi daftar URL API
    :param output_file: Nama file untuk menyimpan hasil proxy mentah
    """
    all_proxies = set()

    try:
        with open(api_file, "r") as file:
            api_urls = file.read().strip().split("\n")

        for api_url in api_urls:
            try:
                response = requests.get(api_url)
                response.raise_for_status()  # Memeriksa jika terjadi error HTTP
                proxies = response.text.strip().split("\n")
                all_proxies.update(proxies)
                print(colored(f"[*] Proxy diambil dari: {api_url}", "magenta"))
            except requests.exceptions.RequestException as e:
                print(colored(f"[!] Gagal mengambil proxy dari {api_url}: {e}", "red"))
    except FileNotFoundError:
        print(colored("[!] File API tidak ditemukan.", "red"))
        return

    if all_proxies:
        with open(output_file, "w") as file:
            file.write("\n".join(all_proxies))
        print(colored(f"[INFO] Proxy mentah berhasil disimpan ke {output_file}", "yellow"))
    else:
        print(colored("[ERROR] Tidak ada proxy yang berhasil diambil.", "red"))

def validate_proxies(input_file, output_file):
    """
    Memvalidasi proxy dari file input dan menyimpan proxy yang valid ke file output.
    :param input_file: Nama file yang berisi proxy mentah
    :param output_file: Nama file untuk menyimpan proxy yang valid
    """
    valid_proxies = []

    try:
        with open(input_file, "r") as file:
            proxies = file.read().strip().split("\n")

        print(colored("[START] Proxy Validation Starting...", "blue"))
        for proxy in proxies:
            # Menyesuaikan proxy URL jika ada "http://"
            if proxy.startswith("http://"):
                proxy = proxy[7:]  # Menghapus "http://"

            # Memisahkan username dan password jika ada
            parsed_proxy = urlparse(proxy)
            username = parsed_proxy.username
            password = parsed_proxy.password
            
            is_valid, protocol = test_proxy(proxy, username, password)
            
            if is_valid:
                # Menyimpan proxy valid dengan format protokol yang digunakan
                valid_proxy = f"{protocol.lower()}://{proxy}"
                valid_proxies.append(valid_proxy)
                time.sleep(0.2)  # Memberi jeda lebih pendek untuk mempercepat validasi

        if valid_proxies:
            with open(output_file, "w") as file:
                file.write("\n".join(valid_proxies))
            print(colored(f"[INFO] Proxy yang valid disimpan ke {output_file}", "magenta"))
        else:
            print(colored("[!] Tidak ada proxy yang valid.", "red"))
    except FileNotFoundError:
        print(colored("[ERROR] File proxy tidak ditemukan.", "red"))

if __name__ == "__main__":
    print_banner()

    # Nama file API dan file hasil
    api_file = "api.txt"
    raw_proxy_file = "get-proxy.txt"
    valid_proxy_file = "valid-proxy.txt"

    # Mengambil proxy dari API dan menyimpannya ke file mentah
    get_proxies(api_file, raw_proxy_file)

    # Memvalidasi proxy dan menyimpan yang valid ke file valid
    validate_proxies(raw_proxy_file, valid_proxy_file)

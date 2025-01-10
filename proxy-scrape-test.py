import requests
from termcolor import colored
import time

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

def test_proxy(proxy):
    """
    Menguji apakah proxy berfungsi.

    :param proxy: Proxy yang akan diuji (format: ip:port)
    :return: True jika proxy berfungsi, False jika tidak
    """
    test_url = "http://httpbin.org/ip"  # URL untuk pengujian proxy
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        response = requests.get(test_url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            print(colored(f"[?] Proxy valid: {proxy}", "green"))
            return True
    except requests.exceptions.RequestException:
        print(colored(f"[?] Proxy invalid: {proxy}", "red"))
    return False

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
                print(colored(f"[?] Proxy diambil dari: {api_url}", "cyan"))
            except requests.exceptions.RequestException as e:
                print(colored(f"[?] Gagal mengambil proxy dari {api_url}: {e}", "red"))
    except FileNotFoundError:
        print(colored("[?] File API tidak ditemukan.", "red"))
        return

    if all_proxies:
        with open(output_file, "w") as file:
            file.write("\n".join(all_proxies))
        print(colored(f"[?] Proxy mentah berhasil disimpan ke {output_file}", "green"))
    else:
        print(colored("[?] Tidak ada proxy yang berhasil diambil.", "red"))

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

        print(colored("\n[??] Menguji proxy...", "yellow"))
        for proxy in proxies:
            if test_proxy(proxy):
                valid_proxies.append(proxy)
                time.sleep(0.5)  # Memberi jeda untuk menghindari batasan server

        if valid_proxies:
            with open(output_file, "w") as file:
                file.write("\n".join(valid_proxies))
            print(colored(f"[?] Proxy yang valid disimpan ke {output_file}", "green"))
        else:
            print(colored("[?] Tidak ada proxy yang valid.", "red"))
    except FileNotFoundError:
        print(colored("[?] File proxy tidak ditemukan.", "red"))

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

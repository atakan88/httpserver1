import subprocess

# Komutları bir dize olarak tanımla
commands = [
    'sudo apt update',
    'sudo pip install --upgrade pip',
    'sudo pip3 install geocoder',
    'sudo pip install psutil',
    'sudo pip install paho-mqtt',
    'sudo pip3 install tb-mqtt-client',
    'pip install pymmh3'
]

# Komutları sırayla çalıştır
for cmd in commands:
    try:
        # Komutu çalıştır ve çıktıları görüntüle
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"Komut başarıyla çalıştırıldı: {cmd}")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Hata durumunda hata mesajını görüntüle
        print(f"Hata oluştu ({cmd}): {e}")
        print(e.stderr)
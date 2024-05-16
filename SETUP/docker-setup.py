import subprocess

# Komutları bir dize olarak tanımla
commands = [
    'mkdir -p ~/.mytb-data && sudo chown -R 799:799 ~/.mytb-data',
    'mkdir -p ~/.mytb-logs && sudo chown -R 799:799 ~/.mytb-logs'
]

# Komutları sırayla çalıştır
for cmd in commands:
    try:
        # Komutu çalıştır ve çıktıları görüntüle
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"Komut başariyla çaliistiirildi: {cmd}")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Hata durumunda hata mesajını görüntüle
        print(f"Hata olustu ({cmd}): {e}")
        print(e.stderr)
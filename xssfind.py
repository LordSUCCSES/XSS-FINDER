import requests
import re

art = '''\
 ____  ___  _________ _________ ___________.___ _______  ________  _____________________ 
\   \/  / /   _____//   _____/ \_   _____/|   |\      \ \______ \ \_   _____/\______   \\
 \     /  \_____  \ \_____  \   |    __)  |   |/   |   \ |    |  \ |    __)_  |       _/
 /     \  /        \/        \  |     \   |   /    |    \|    `   \|        \ |    |   \\
/___/\  \/_______  /_______  /  \___  /   |___\____|__  /_______  /_______  / |____|_  /
      \_/        \/        \/       \/                \/        \/        \/         \/ '''

print(art)

url = input('Url Ve Payload Girin (Örnek: https://www.deneme.com/deneme.php?param=<script>alert(""mera"");</script>): ')

response = requests.get(url)

if response.status_code == 200:
    content = response.text

    aranan_kelime = 'alert'

    if re.search(aranan_kelime, content, re.IGNORECASE):
        print(f"{url} Url'sinde XSS Zafiyeti Mevcut!")
        with open("bulundu.txt" ,"w") as dosya:
            dosya.write(url)
    else:
        print(f"{url} Url'sinde XSS Zafiyeti Mevcut Değil")
else:
    print(f"URL'ye erişilemedi")

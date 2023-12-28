import requests
import re

class Color:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"

art = '''\
 ____  ___  _________ _________ ___________.___ _______  ________  _____________________ 
\   \/  / /   _____//   _____/ \_   _____/|   |\      \ \______ \ \_   _____/\______   \\
 \     /  \_____  \ \_____  \   |    __)  |   |/   |   \ |    |  \ |    __)_  |       _/
 /     \  /        \/        \  |     \   |   /    |    \|    `   \|        \ |    |   \\
/___/\  \/_______  /_______  /  \___  /   |___\____|__  /_______  /_______  / |____|_  /
      \_/        \/        \/       \/                \/        \/        \/         \/ '''

print(Color.BROWN + art + Color.GREEN)

url = input('Url Ve Payload Girin (Örnek: https://www.deneme.com/deneme.php?param=<script>alert(""mera"");</script>): ')

response = requests.get(url)

if response.status_code == 200:
    content = response.text

    aranan_kelime = 'alert'

    if re.search(aranan_kelime, content, re.IGNORECASE):
        print(Color.BLUE + f"{url} Url'sinde XSS Zafiyeti Mevcut!")
        with open("bulundu.txt" ,"w") as dosya:
            dosya.write(url)
    else:
        print(Color.RED + f"{url} Url'sinde XSS Zafiyeti Mevcut Değil")
else:
    print(Color.RED + f"URL'ye erişilemedi")

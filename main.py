from services.open_weather import fetch_weather
from services.excel_file import append_to_excel
import time

# CRON
while True:
    weather = fetch_weather()
    append_to_excel(weather)
    print("Pobrano nowe dane")
    time.sleep(10)

# tworzenie repozytorium
# git init

# sprawedzanie stanu repozytorium
# git status

# dodanie pliku do repo
# git add nazwa

# dodanie wszystkiego
# git add .

#stworzenie commita - punkt w czasie do którego można wracać
# git commit -m "wiadomosc"

# lista commitów
# git log --oneline

#  podróżowanie po commitach
# git checkout id_commita

# powrót do teraźniejszości
# git checkout -



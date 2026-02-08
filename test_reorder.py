import requests
import json
import time

# --- KONFIGURATION ---
AWTRIX_IP = "192.168.178.191"  # Hier die IP deiner Awtrix eintragen
# ---------------------

BASE_URL = f"http://{AWTRIX_IP}/api/custom"

def create_app(name, text, color):
    payload = {
        "text": text,
        "color": color,
        "duration": 5
    }
    
    print(f"Erstelle App: {name}...")
    try:
        response = requests.post(
            f"{BASE_URL}?name={name}", 
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            print(f"Erfolg: {name} angelegt.")
        else:
            print(f"Fehler bei {name}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Verbindungsfehler: {e}")

def main():
    # 5 verschiedene Test-Apps definieren
    test_apps = [
        ("Test1", "EINS", [255, 0, 0]),    # Rot
        ("Test2", "ZWEI", [0, 255, 0]),    # Grün
        ("Test3", "DREI", [0, 0, 255]),    # Blau
        ("Test4", "VIER", [255, 255, 0]),  # Gelb
        ("Test5", "FUNF", [255, 0, 255])   # Magenta
    ]

    for name, text, color in test_apps:
        create_app(name, text, color)
        time.sleep(0.3)

    print("Alle Apps erstellt!")
    print("1. Gehe jetzt ins Webinterface -> App Loop.")
    print("2. Sortiere die Apps um.")
    print("3. Starte die Awtrix neu.")
    print("4. Die Reihenfolge sollte exakt so bleiben wie eingestellt.")

if __name__ == "__main__":
    main()

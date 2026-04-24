# AWTRIX 3 - Guía de Desarrollo

## Repositorio
- **Fork:** https://github.com/XE1E/awtrix3
- **Original:** https://github.com/Blueforcer/awtrix3
- **Documentación:** https://blueforcer.github.io/awtrix3/

## Requisitos

### Software
1. **VS Code** con extensión **PlatformIO IDE**
   - O instalar PlatformIO CLI: `pip install platformio`

2. **Drivers USB**
   - CP2102 (para Ulanzi TC001)
   - CH340 (para ESP32 D1 Mini genérico)

### Hardware compatible
| Placa | Entorno PlatformIO |
|-------|-------------------|
| Ulanzi TC001 | `ulanzi` |
| ESP32 D1 Mini (upgrade AWTRIX 2) | `awtrix2_upgrade` |

## Estructura del código fuente

```
src/
├── main.cpp              # Punto de entrada, setup() y loop()
├── DisplayManager.cpp    # Control matriz LED (72KB - archivo principal)
├── Apps.cpp              # Sistema de aplicaciones personalizadas
├── MQTTManager.cpp       # Integración MQTT / Home Assistant
├── ServerManager.cpp     # API HTTP REST
├── PeripheryManager.cpp  # Sensores, botones, buzzer
├── MenuManager.cpp       # Menú en pantalla
├── Overlays.cpp          # Notificaciones superpuestas
├── effects.cpp           # Efectos visuales (45KB)
├── GifPlayer.h           # Reproductor de GIFs
├── AwtrixFont.h          # Fuente de texto
└── Globals.cpp           # Variables globales y configuración
```

## Comandos de compilación

```bash
# Navegar al proyecto
cd D:\Documents\Raspi\awtrix\awtrix3

# Compilar para Ulanzi TC001
pio run -e ulanzi

# Compilar para ESP32 D1 Mini (upgrade AWTRIX 2)
pio run -e awtrix2_upgrade

# Compilar y subir al dispositivo
pio run -e ulanzi --target upload

# Monitor serial (debug)
pio device monitor
```

## Sincronizar con upstream

```bash
# Obtener cambios del repositorio original
git fetch upstream

# Fusionar cambios a tu rama main
git checkout main
git merge upstream/main

# Subir a tu fork
git push origin main
```

## Librerías principales

| Librería | Uso |
|----------|-----|
| FastLED | Control de LEDs WS2812B |
| FastLED NeoMatrix | Matriz LED |
| ArduinoJson | Parsing JSON (API/MQTT) |
| PubSubClient | Cliente MQTT |
| EasyButton | Manejo de botones |
| Adafruit BME280/BMP280/SHT31 | Sensores de temperatura |

## Archivos clave para modificar

- **Apps.cpp** - Agregar aplicaciones personalizadas
- **effects.cpp** - Crear nuevos efectos visuales
- **DisplayManager.cpp** - Modificar comportamiento de pantalla
- **Globals.cpp** - Agregar nuevas configuraciones

## Notas

- El proyecto usa ESP32 con Arduino framework
- CPU a 240MHz
- Tamaño máximo paquete MQTT: 8192 bytes
- Puerto monitor serial: 115200 baud

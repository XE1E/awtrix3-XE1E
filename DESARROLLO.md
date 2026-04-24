# AWTRIX 3 - Guía de Instalación y Desarrollo

## Repositorio
- **Tu Fork:** https://github.com/XE1E/awtrix3
- **Original:** https://github.com/Blueforcer/awtrix3
- **Documentación:** https://blueforcer.github.io/awtrix3/

---

# PARTE 1: INSTALACIÓN CON ESP32 + MATRIZ WS2812B 32x8

## Materiales necesarios

| Componente | Descripción | Notas |
|------------|-------------|-------|
| ESP32 | ESP32-WROOM, NodeMCU-32S, o ESP32 D1 Mini | Cualquier variante funciona |
| Matriz LED | WS2812B 32x8 (256 LEDs) | Flexible o rígida |
| Fuente 5V | 5V 4A mínimo | Los LEDs consumen ~60mA cada uno a brillo máximo |
| Cables | Dupont o soldados | 3 cables: VCC, GND, DATA |
| Capacitor | 1000µF 6.3V (opcional) | Protege los LEDs de picos |
| Resistencia | 330Ω (opcional) | En línea de datos, protege el primer LED |

## Diagrama de conexión

```
                    ESP32                         MATRIZ WS2812B 32x8
                 +---------+                      +------------------+
                 |         |                      |                  |
    USB -------->|   USB   |                      |   32 x 8 LEDs    |
                 |         |                      |                  |
                 |  GPIO32 |---[330Ω]------------>| DIN (Data In)    |
                 |         |                      |                  |
                 |    GND  |--------------------->| GND              |
                 |         |                      |                  |
                 |    5V   |--------------------->| 5V / VCC         |
                 +---------+                      +------------------+
                      |                                   |
                      +----------- GND común -------------+
                                      |
                               [1000µF cap]
                                      |
                              Fuente 5V 4A
```

## Conexiones pin a pin

| ESP32 GPIO | Conectar a | Descripción |
|------------|------------|-------------|
| **GPIO32** | DIN de la matriz | Datos de los LEDs (obligatorio) |
| **GND** | GND de la matriz Y fuente | Tierra común (obligatorio) |
| **5V/VIN** | 5V de la fuente | Alimentación (obligatorio) |

### Conexiones opcionales (mejoran la experiencia)

| ESP32 GPIO | Componente | Descripción |
|------------|------------|-------------|
| GPIO35 | LDR (fotoresistor GL5516) | Brillo automático según luz ambiente |
| GPIO26 | Botón izquierdo | Navegación menú |
| GPIO27 | Botón central | Seleccionar |
| GPIO14 | Botón derecho | Navegación menú |
| GPIO15 | Buzzer pasivo | Sonidos y alarmas |
| GPIO21 (SDA) | Sensor temp (BME280/SHT31) | Temperatura y humedad |
| GPIO22 (SCL) | Sensor temp (BME280/SHT31) | I2C Clock |

## Paso 1: Preparar el hardware

1. **Conecta la matriz al ESP32:**
   - GPIO32 → DIN de la matriz (con resistencia 330Ω opcional)
   - GND del ESP32 → GND de la matriz
   
2. **Conecta la fuente de alimentación:**
   - 5V de la fuente → 5V de la matriz
   - GND de la fuente → GND de la matriz Y GND del ESP32
   - (El ESP32 se puede alimentar por USB o por la fuente)

3. **Importante:** GND debe ser común entre ESP32, matriz y fuente.

## Paso 2: Flashear el firmware

### Opción A: Flasher online (más fácil)

1. Abre Google Chrome o Microsoft Edge
2. Ve a: https://blueforcer.github.io/awtrix3/#/flasher
3. Conecta el ESP32 por USB
4. Selecciona el puerto COM
5. Marca "Erase" si es la primera vez
6. Haz clic en "Flash"

### Opción B: Compilar desde código (para desarrollo)

```bash
# 1. Instalar PlatformIO en VS Code
#    - Abre VS Code
#    - Ve a Extensions (Ctrl+Shift+X)
#    - Busca "PlatformIO IDE"
#    - Instalar

# 2. Abrir el proyecto
#    - File > Open Folder > D:\Documents\Raspi\awtrix\awtrix3

# 3. Compilar (desde terminal de PlatformIO)
cd D:\Documents\Raspi\awtrix\awtrix3
pio run -e ulanzi

# 4. Subir al ESP32 (conectado por USB)
pio run -e ulanzi --target upload

# 5. Ver logs de debug
pio device monitor
```

## Paso 3: Configurar WiFi

1. Después de flashear, el ESP32 crea una red WiFi:
   - **Nombre:** `awtrix_XXXXX`
   - **Contraseña:** `12345678`

2. Conéctate a esa red desde tu celular o PC

3. Abre el navegador y ve a: `http://192.168.4.1`

4. Ingresa los datos de tu WiFi y guarda

5. El dispositivo se reinicia y se conecta a tu red

## Paso 4: Acceder a la interfaz web

1. Busca la IP del dispositivo (aparece en la matriz al conectar)
2. Abre `http://[IP-DEL-DISPOSITIVO]` en tu navegador
3. Configura MQTT, apps, y otras opciones

## Solución de problemas

### La matriz muestra caracteres raros o invertidos

Crea un archivo `dev.json` en el administrador de archivos web con:

```json
{
  "matrix": 2
}
```

Prueba con valores 0, 1, o 2 hasta que se vea correctamente.

### No enciende ningún LED

- Verifica que GPIO32 esté conectado a DIN
- Verifica que GND sea común
- Verifica que la fuente tenga suficiente corriente (4A)

### El ESP32 se reinicia constantemente

- La fuente no tiene suficiente corriente
- Baja el brillo en la configuración

---

# PARTE 2: DESARROLLO Y MODIFICACIÓN

## Estructura del código fuente

```
src/
├── main.cpp              # Punto de entrada, setup() y loop()
├── DisplayManager.cpp    # Control matriz LED (archivo principal)
├── Apps.cpp              # Sistema de aplicaciones
├── MQTTManager.cpp       # Integración MQTT / Home Assistant
├── ServerManager.cpp     # API HTTP REST
├── PeripheryManager.cpp  # Sensores, botones, buzzer
├── MenuManager.cpp       # Menú en pantalla
├── Overlays.cpp          # Notificaciones superpuestas
├── effects.cpp           # Efectos visuales
├── GifPlayer.h           # Reproductor de GIFs
└── Globals.cpp           # Variables globales
```

## Archivos clave para modificar

| Archivo | Para qué modificarlo |
|---------|---------------------|
| `Apps.cpp` | Crear nuevas aplicaciones |
| `effects.cpp` | Agregar efectos visuales |
| `DisplayManager.cpp` | Cambiar comportamiento de pantalla |
| `PeripheryManager.cpp` | Agregar sensores o botones |
| `Globals.cpp` | Nuevas configuraciones globales |

## Comandos de compilación

```bash
# Compilar sin subir
pio run -e ulanzi

# Compilar y subir
pio run -e ulanzi --target upload

# Solo subir (si ya compilaste)
pio run -e ulanzi --target uploadfs

# Monitor serial (115200 baud)
pio device monitor

# Limpiar build
pio run -e ulanzi --target clean
```

## Sincronizar con el repositorio original

```bash
# Obtener cambios del repo original
git fetch upstream

# Fusionar a tu rama
git checkout main
git merge upstream/main

# Subir a tu fork
git push origin main
```

## Librerías principales

| Librería | Uso |
|----------|-----|
| FastLED | Control de LEDs WS2812B |
| FastLED NeoMatrix | Gestión de matriz |
| ArduinoJson | Parsing JSON |
| PubSubClient | Cliente MQTT |
| EasyButton | Manejo de botones |
| Adafruit BME280/SHT31 | Sensores de temperatura |

## Notas técnicas

- CPU: ESP32 a 240MHz
- Framework: Arduino
- Tamaño máximo paquete MQTT: 8192 bytes
- Puerto serial: 115200 baud
- Pin matriz LED: GPIO32 (hardcoded en DisplayManager.cpp línea 40)

# Changelog - Gemini CLI Session (February 2026)

## 🚀 Persistent App Loop Order (Issue #757)
Awtrix now features a centralized and persistent app loop management system (stored in `apps.json`). This ensures your carefully arranged app sequence is never lost and survives every reboot.

### Key Features for Users:
*   **True Persistence:** Your app order is saved immediately upon any change and restored exactly as it was after every reboot.
*   **"Ghost App" Reservation:** You can now include apps in your loop that are currently offline or haven't sent data yet. Awtrix "reserves" their spot. As soon as the app becomes available (via API/MQTT), it appears in its designated position.
*   **Seamless Skipping:** If an app is in your list but has no data, Awtrix automatically skips it. No more black screens or "hanging" on missing apps.
*   **Duplicate Support:** You can now easily repeat apps in the loop (e.g., `Time, Weather, Time, Battery`) to see important information more frequently.
*   **Authoritative Control:** The Web UI and reorder API now give you full control over all configured apps (including offline ones). Removing an app from the list will permanently delete its configuration.

### New Reorder API (HTTP & MQTT)
You can now reorder your entire loop using either HTTP or MQTT by sending a JSON array:
*   **HTTP POST:** `http://[IP]/api/reorder`
*   **MQTT Topic:** `[PREFIX]/reorder` (e.g., `awtrix/reorder`)
*   **Payload Example:** `["Time", "MyCustomApp", "Time", "Date"]`

---

## ⚡ Connectivity & Stability
*   **Auto-Reconnect Watchdog:** A new background task monitors your WiFi every 30 seconds. If the connection drops (e.g., router restart), Awtrix will now actively attempt to reconnect (#405, #765).
*   **Global WiFi Support:** Unlocked WiFi channels 12 and 13. Awtrix is now fully compatible with European and Asian network regulations.
*   **Hidden Network Support:** The WiFi scanner in the web interface now detects and displays hidden SSIDs.
*   **Latency Optimization:** Optimized WiFi Power-Saving initialization to prevent lag spikes and improve MQTT responsiveness (#765).

## 🐛 Bug Fixes
*   **TMODE 5 Color Fix:** The "Big Time" clock style now correctly respects the user-defined `TIME_COLOR` setting for its background (#759).
*   **Font Alignment:** Adjusted the Tilde (`~`) character position down by one pixel for better vertical centering (#754).
*   **AP Mode Stabilization:** Fixed a bug where the device could enter an infinite reboot loop when failing to connect to a WiFi network.
*   **API Data Consistency:** Fixed `/api/loop` to return a proper JSON Array, ensuring that duplicate app entries are reported correctly.
*   **API Metadata:** Added an `active` flag to the app list API, allowing external systems to distinguish between running apps and reserved "Ghost" apps.

---
*All changes have been integrated into the source code and are ready for the next firmware build.*

#include <ESP8266WiFi.h>
#include <WebSocketsClient.h>

const char* ssid = "DEIN_WLAN";
const char* password = "DEIN_PASSWORT";

WebSocketsClient ws;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nVerbunden mit WLAN");

  ws.begin("midnight-worker", 443, "/", "wss"); // Host, Port, Pfad, Protokolltyp
  ws.onEvent(onWsEvent);
}

void loop() {
  ws.loop();
}

void onWsEvent(WStype_t type, uint8_t * payload, size_t length) {
  if (type == WStype_CONNECTED) {
    Serial.println("WebSocket verbunden!");
    ws.sendTXT("Hallo Welt");
  } 
  else if (type == WStype_TEXT) {
    Serial.printf("Empfangen: %s\n", payload);
  }
}


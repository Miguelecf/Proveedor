from kafka import KafkaConsumer
import json
import time 

# Configuración del consumidor
consumer = KafkaConsumer(
    'orden-de-compra',  # Tópico al que se conecta
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # Comienza desde el principio del log
    enable_auto_commit=True,
    group_id='ordenes-group',  # Grupo de consumidores (cambia si necesitas otro)
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Esperando mensajes del tópico 'orden-de-compra'...")
for message in consumer:
    # message.value contiene el cuerpo del mensaje
    order_data = message.value
    store_code = order_data.get("store_code")
    order_id = order_data.get("order_id")
    items = order_data.get("items", [])
    request_date = order_data.get("request_date")
    observations = order_data.get("observations")  # Agregado para obtener las observaciones
    
    # Procesar la información de la orden
    print(f"\nNueva orden recibida:")
    print(f"Código de tienda: {store_code}")
    print(f"ID de la orden: {order_id}")
    print(f"Fecha de solicitud: {request_date}")
    print(f"Observaciones: {observations}")  # Agregado para imprimir observaciones
    print(f"Ítems solicitados:")
    for item in items:
        print(f"- Código de ítem: {item.get('item_code')}, Color: {item.get('color')}, "
              f"Talla: {item.get('size')}, Cantidad: {item.get('quantity')}")

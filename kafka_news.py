from kafka import KafkaProducer
import json

# Configuración del productor
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Función para enviar mensajes a Kafka
def send_news_to_kafka(product_code, sizes, photo_urls):
    message = {
        "product_code": product_code,  # Usamos 'product_code' para el código del producto
        "sizes": sizes,  # Lista de talles con sus colores
        "photo_urls": photo_urls  # Lista de URLs de fotos
    }
    producer.send('novedades', value=message)
    producer.flush()
    print(f"Mensaje enviado a Kafka: {message}")

# Función para procesar la novedad y enviarla a Kafka
def process_new(new, product_repository):
    """
    Procesa una novedad (producto nuevo) y envía un mensaje al tópico de Kafka si el producto existe.
    
    Parameters:
    - new: instancia del producto nuevo que contiene el código único del producto (`unique_code`).
    - product_repository: repositorio para obtener información del producto basado en el código.
    """
    try:
        # Obtén el producto por su unique_code
        product = product_repository.get_product_by_code(new.unique_code)

        if not product:
            raise ValueError("Product not found.")

        # Crear la estructura para los talles y colores
        sizes = [
            {
                "size": product.size,  # Talle del producto
                "colors": [product.color]  # Colores asociados al talle
            }
        ]
        
        # Crear la lista de URLs de fotos
        photo_urls = [product.image_url]  # URLs de fotos del producto
        
        # Llama a la función de enviar el mensaje a Kafka
        send_news_to_kafka(
            product_code=product.unique_code,  # Usamos 'unique_code' como 'product_code'
            sizes=sizes,
            photo_urls=photo_urls
        )

    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

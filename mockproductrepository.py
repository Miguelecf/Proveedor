from kafka_news import send_news_to_kafka

class MockProductRepository:
    def get_product_by_code(self, unique_code):
        # Simulamos un producto que obtendremos de la base de datos
        # Ahora devolvemos el formato correcto para 'sizes' y 'photo_urls'
        return Product(unique_code="12345", size="M", colors='Red', 
                        image_url=["http://example.com/image.jpg","http://google.com/image2.jpg","http://mercadolibre.com/321.jpg"])

class Product:
    def __init__(self, unique_code, size, colors, image_url):
        self.unique_code = unique_code
        self.size = size
        self.colors = colors
        self.image_url = image_url

# Inicializar el repositorio de prueba y llamar a la función
if __name__ == "__main__":
    product_repository = MockProductRepository()

    # Simulamos obtener un producto por código único
    product = product_repository.get_product_by_code("12345")

    # Adaptamos el producto al formato esperado por 'send_news_to_kafka'
    sizes = [{
        "size": product.size,  # El talle del producto
        "colors": ["Blue","Orange","Red"]  # Lista de colores para ese talle
    }]
    photo_urls = [product.image_url]  # Lista de URLs de fotos

    # Llamamos a 'send_news_to_kafka' con los datos adaptados
    send_news_to_kafka(
        product_code=product.unique_code,  # Usamos 'unique_code' como 'product_code'
        sizes=sizes,  # Lista de talles con colores
        photo_urls=photo_urls  # Lista de URLs de fotos
    )



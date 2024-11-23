from app.db.session import engine, Base
from app.models.user import User, UserRole
from app.models.client import Client
from app.models.category import Category
from app.models.product import Product
from app.models.order import Order, PaymentMethod, OrderStatus
from app.models.order_product import OrderProduct

# El resto del código sigue igual
# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

# Iniciar una sesión
session = Session(bind=engine)

# Datos de prueba
try:
    # Usuarios
    admin = User(
        name="Admin",
        email="admin@example.com",
        hashed_password="hashed_admin",
        role=UserRole.administrator,
    )
    barista = User(
        name="Barista",
        email="barista@example.com",
        hashed_password="hashed_barista",
        role=UserRole.barista,
    )
    waiter = User(
        name="Waiter",
        email="waiter@example.com",
        hashed_password="hashed_waiter",
        role=UserRole.waiter,
    )
    session.add_all([admin, barista, waiter])

    # Clientes
    client1 = Client(
        name="John Doe",
        phone="123456789",
        email="john.doe@example.com",
        loyaltyPoints=10,
    )
    client2 = Client(
        name="Jane Smith",
        phone="987654321",
        email="jane.smith@example.com",
        loyaltyPoints=5,
    )
    session.add_all([client1, client2])

    # Categorías
    drinks = Category(name="Drinks")
    pastries = Category(name="Pastries")
    session.add_all([drinks, pastries])

    # Productos
    coffee = Product(
        name="Coffee", categoryId=1, basePrice=3.5, size="Medium", margin=1.5
    )
    croissant = Product(name="Croissant", categoryId=2, basePrice=2.0, margin=1.0)
    session.add_all([coffee, croissant])

    # Ordenes
    order1 = Order(
        clientId=1,
        baristaId=2,
        totalPrice=5.0,
        paymentMethod=PaymentMethod.cash,
        status=OrderStatus.completed,
    )
    session.add(order1)

    # Relación orden-producto
    order_product1 = OrderProduct(orderId=1, productId=1, quantity=1, finalPrice=3.5)
    order_product2 = OrderProduct(orderId=1, productId=2, quantity=1, finalPrice=2.0)
    session.add_all([order_product1, order_product2])

    # Confirmar cambios
    session.commit()

    print("Datos de prueba insertados correctamente.")
except Exception as e:
    session.rollback()
    print(f"Error al insertar datos: {e}")
finally:
    session.close()

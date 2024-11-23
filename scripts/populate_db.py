from sqlalchemy.orm import Session
from app.db.session import engine, Base
from app.models.user import User, UserRole
from app.models.client import Client
from app.models.category import Category
from app.models.product import Product
from app.models.order import Order, PaymentMethod, OrderStatus
from app.models.order_product import OrderProduct

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

# Iniciar una sesión
session = Session(bind=engine)

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
    session.commit()  # Confirmar para obtener IDs

    # Clientes
    client1 = Client(
        name="John Doe",
        phone="123456789",
        email="john.doe@example.com",
        loyalty_points=10,  # snake_case adaptado
    )
    client2 = Client(
        name="Jane Smith",
        phone="987654321",
        email="jane.smith@example.com",
        loyalty_points=5,  # snake_case adaptado
    )
    session.add_all([client1, client2])
    session.commit()

    # Categorías
    drinks = Category(name="Drinks")
    pastries = Category(name="Pastries")
    session.add_all([drinks, pastries])
    session.commit()

    # Productos
    coffee = Product(
        name="Coffee",
        category_id=drinks.id,
        base_price=3.5,  # snake_case adaptado
        size="Medium",
        margin=1.5,
    )
    croissant = Product(
        name="Croissant",
        category_id=pastries.id,
        base_price=2.0,  # snake_case adaptado
        margin=1.0,
    )
    session.add_all([coffee, croissant])
    session.commit()

    # Órdenes
    order1 = Order(
        client_id=client1.id,  # snake_case adaptado
        barista_id=barista.id,  # snake_case adaptado
        total_price=5.0,  # snake_case adaptado
        payment_method=PaymentMethod.cash,  # Enum
        status=OrderStatus.completed,  # Enum
    )
    session.add(order1)
    session.commit()  # Confirmar para obtener el ID de la orden

    # Relación orden-producto
    order_product1 = OrderProduct(
        order_id=order1.id,
        product_id=coffee.id,
        quantity=1,
        final_price=3.5,
    )
    order_product2 = OrderProduct(
        order_id=order1.id,
        product_id=croissant.id,
        quantity=1,
        final_price=2.0,
    )
    session.add_all([order_product1, order_product2])
    session.commit()

    print("Datos de prueba insertados correctamente.")
except Exception as e:
    session.rollback()
    print(f"Error al insertar datos: {e}")
finally:
    session.close()

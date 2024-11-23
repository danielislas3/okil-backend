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
    if not session.query(User).filter_by(email="admin@example.com").first():
        admin = User(
            name="Admin",
            email="admin@example.com",
            hashed_password="hashed_admin",
            role=UserRole.administrator,
        )
        session.add(admin)

    if not session.query(User).filter_by(email="barista@example.com").first():
        barista = User(
            name="Barista",
            email="barista@example.com",
            hashed_password="hashed_barista",
            role=UserRole.barista,
        )
        session.add(barista)

    if not session.query(User).filter_by(email="waiter@example.com").first():
        waiter = User(
            name="Waiter",
            email="waiter@example.com",
            hashed_password="hashed_waiter",
            role=UserRole.waiter,
        )
        session.add(waiter)
    session.commit()

    # Clientes
    if not session.query(Client).filter_by(email="john.doe@example.com").first():
        client1 = Client(
            name="John Doe",
            phone="123456789",
            email="john.doe@example.com",
            loyalty_points=10,
        )
        session.add(client1)

    if not session.query(Client).filter_by(email="jane.smith@example.com").first():
        client2 = Client(
            name="Jane Smith",
            phone="987654321",
            email="jane.smith@example.com",
            loyalty_points=5,
        )
        session.add(client2)
    session.commit()

    # Categorías
    if not session.query(Category).filter_by(name="Drinks").first():
        drinks = Category(name="Drinks")
        session.add(drinks)

    if not session.query(Category).filter_by(name="Pastries").first():
        pastries = Category(name="Pastries")
        session.add(pastries)
    session.commit()

    # Productos
    drinks = session.query(Category).filter_by(name="Drinks").first()
    pastries = session.query(Category).filter_by(name="Pastries").first()

    if not session.query(Product).filter_by(name="Coffee").first():
        coffee = Product(
            name="Coffee",
            category_id=drinks.id,
            base_price=3.5,
            size="Medium",
            margin=1.5,
        )
        session.add(coffee)

    if not session.query(Product).filter_by(name="Croissant").first():
        croissant = Product(
            name="Croissant",
            category_id=pastries.id,
            base_price=2.0,
            margin=1.0,
        )
        session.add(croissant)
    session.commit()

    # Órdenes
    client1 = session.query(Client).filter_by(email="john.doe@example.com").first()
    barista = session.query(User).filter_by(email="barista@example.com").first()

    if not session.query(Order).filter_by(client_id=client1.id).first():
        order1 = Order(
            client_id=client1.id,
            barista_id=barista.id,
            total_price=5.0,
            payment_method=PaymentMethod.cash,
            status=OrderStatus.completed,
        )
        session.add(order1)
        session.commit()

        # Relación orden-producto
        coffee = session.query(Product).filter_by(name="Coffee").first()
        croissant = session.query(Product).filter_by(name="Croissant").first()

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

from app import app
from models import db, Product

with app.app_context():
    db.drop_all()
    db.create_all()

    products = [
        Product(brand="Ajanta", model="Digital Pro", category="Digital",
                features="Backlight, Alarm, Stopwatch", price=49.99, image="watch1.jpg"),
        Product(brand="Ajanta", model="Classic Analog", category="Analog",
                features="Leather strap, Water resistant", price=79.99, image="watch2.jpg"),
        Product(brand="Ajanta", model="Smart X", category="Smart",
                features="Heart rate monitor, Bluetooth", price=129.99, image="watch3.jpg"),
        Product(brand="Ajanta", model="Sport Digital", category="Digital",
                features="Shock resistant, LED display", price=59.99, image="watch4.jpg"),
        Product(brand="Ajanta", model="Luxury Analog", category="Analog",
                features="Stainless steel, Sapphire glass", price=149.99, image="watch5.jpg")
    ]

    db.session.add_all(products)
    db.session.commit()
    print("Database seeded with 5 watches")

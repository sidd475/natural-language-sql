# seed.py
import random
from datetime import date

from faker import Faker

from app.database import SessionLocal, engine
from app.models import Employee, Product, Sale

print("Populating the database with mock data...")

fake = Faker()

# Create a session to interact with the database
db_session = SessionLocal()

# Create and add 10 employees
employees = []
for _ in range(10):
    emp = Employee(
        name=fake.name(),
        department=random.choice(["Sales", "Marketing", "Engineering"]),
        start_date=fake.date_between(start_date="-5y", end_date="today"),
    )
    employees.append(emp)
db_session.add_all(employees)
db_session.commit()

# Create and add 20 products
products = []
categories = ["Electronics", "Clothing", "Books", "Home Goods"]
for _ in range(20):
    prod = Product(
        name=fake.word() + " " + fake.word(),
        category=random.choice(categories),
        price=round(random.uniform(10.0, 1000.0), 2),
    )
    products.append(prod)
db_session.add_all(products)
db_session.commit()

# Create 100 random sales
for _ in range(100):
    sale = Sale(
        product_id=random.choice(products).id,
        employee_id=random.choice(employees).id,
        quantity=random.randint(1, 10),
        sale_date=fake.date_between(start_date="-1y", end_date="today"),
    )
    db_session.add(sale)

db_session.commit()
db_session.close()

print("Mock data populated successfully!")

# app/models.py
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base  # Import Base from the correct file


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    department = Column(String)
    start_date = Column(Date)

    sales = relationship("Sale", back_populates="employee")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)

    sales = relationship("Sale", back_populates="product")


class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    quantity = Column(Integer)
    sale_date = Column(Date)

    product = relationship("Product", back_populates="sales")
    employee = relationship("Employee", back_populates="sales")

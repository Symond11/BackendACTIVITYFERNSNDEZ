from sqlmodel import Field , SQLModel


class Customer(SQLModel, table=True):
    customer_id: int | None = Field(default=None, primary_key=True)
    name: str
    address: str
    gender: str
    age: int | None = None

class DeliveryRider(SQLModel, table=True):
    deliveryrider_id: int | None = Field(default=None, primary_key=True)
    name: str
    gender: str
    transpo_model: str
    age: int | None = None

class Order(SQLModel, table=True):
    order_id: int | None = Field(default=None, primary_key=True)
    order_name: str
    company: str
    quantity: int | None = None
    price: int | None = None

from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine

from models import Customer, DeliveryRider, Order

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/customer/{id}")
async def read_customer(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        cust = session.get(Customer, id)
        return {"message": cust}

@app.post("/customer")
async def root(customer  : Customer):
    with Session(engine) as session:
        session.add(customer)
        session.commit()
        session.refresh(customer)

        return {"message": 'created'}

@app.get("/deliveryrider/{id}")
async def read_deliveryrider(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        dr = session.get(DeliveryRider, id)
        return {"message": dr}

@app.post("/deliveryrider")
async def root(deliveryrider : DeliveryRider):
    with Session(engine) as session:
        session.add(deliveryrider)
        session.commit()
        session.refresh(deliveryrider)

        return {"message": 'created'}

@app.get("/order/{id}")
async def read_order(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        ordd = session.get(Order, id)
        return {"message": ordd}

@app.post("/order")
async def root(order  : Order):
    with Session(engine) as session:
        session.add(order)
        session.commit()
        session.refresh(order)

        return {"message": 'created'}
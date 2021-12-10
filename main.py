from Car import Car
from sqlalchemy import text
from db_cofig import local_session, create_all_entities

# create tables
create_all_entities()

# local_session.add(User(username='bob', email='bob@bob.com'))
# local_session.commit()

# add a list of cars
cars_list = [Car(model='mustang', brand='ford', year = 1989), Car(model='500', brand='fiat', year = 2009)]
local_session.add_all(cars_list)
local_session.commit()

# delete a cars
local_session.query(Car).filter(Car.id == 2).delete(synchronize_session=False)
local_session.commit()

# print all cars
users = local_session.query(Car).all()
print(cars)

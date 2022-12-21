from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from yelp import models

engine = create_engine('sqlite:///./restaurants.sqlite')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if __name__ == "__main__":
    with SessionLocal() as db:

        print(db.query(models.Restaurant)\
                .where(models.Restaurant.cuisine_style == 'Italian', models.Restaurant.city == 'Paris')\
                .all() )

        # new_restaurant = models.Restaurant(name = 'Tantura', cuisine_style = 'Middle Eastern', city = 'Lisbon')
        # db.add(new_restaurant)
        # db.commit()
        # db.refresh(new_restaurant)
        # print(new_restaurant)

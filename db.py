import databases
import sqlalchemy
from decouple import config

DATABASE_URL = f"postgresql://{config('DB_USER')}:" \
               f"{config('DB_PASSWORD')}@" \
               f"{config('DB_SERVER')}:" \
               f"{config('DB_PORT')}/" \
               f"{config('DB_DATABASE')}"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# localhost
# 5432
# compaints
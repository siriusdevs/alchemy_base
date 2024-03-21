import os

import dotenv
from sqlalchemy import create_engine


def get_db_url() -> str:
    dotenv.load_dotenv()
    PG_VARS = 'PG_HOST', 'PG_PORT', 'PG_USER', 'PG_PASSWORD', 'PG_DBNAME'
    credentials = {var: os.environ.get(var) for var in PG_VARS}
    return 'postgresql+psycopg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DBNAME}'.format(**credentials)


if __name__ == '__main__':
    engine = create_engine(get_db_url())

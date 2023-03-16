from databases import Database
from pydantic import BaseSettings, SecretStr
from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table, create_engine  # type: ignore
from sqlalchemy.sql import func  # type: ignore


class DBSettings(BaseSettings):
    server: str = "localhost"
    user: str = "jason"
    password: SecretStr = SecretStr("")
    db: str = "hello_fastapi_dev"
    port: int = 5432
    pool_size: int = 10
    max_overflow: int = 10

    @property
    def url(self) -> str:
        return "postgresql://{}:{}@{}:{}/{}".format(
            self.user, self.password.get_secret_value(), self.server, self.port, self.db
        )


db_settings = DBSettings()

DATABASE_URL = db_settings.url

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)  # type: ignore

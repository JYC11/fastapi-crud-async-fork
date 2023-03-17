from pydantic import BaseSettings, SecretStr, Field


class DBSettings(BaseSettings):
    server: str = Field(..., env="POSTGRES_SERVER")
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

    class Config:
        env_prefix = "postgres_"
        env_file = ".env"

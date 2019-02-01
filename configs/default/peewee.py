DB_HOST = "mysql"
DB_NAME = "anteater"
DB_USER = "root"
DB_PASSWORD = "toor333666"

PW_DB_URL = "mysql+pool://{user}:{password}@{host}/{name}".format(
    host=DB_HOST, name=DB_NAME, user=DB_USER, password=DB_PASSWORD
)
PW_CONN_PARAMS = {"charset": "utf8mb4", "stale_timeout": 1800}
PW_MODEL = "peeweext.model.Model"

from app.drivers.mongo import MongoDriver as Driver

listeners = [
    (Driver.register_db, "before_server_start"),
]

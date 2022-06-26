from app.db.mongo import store as mongo_store

repositories = {}
repositories.update(mongo_store.repositories)

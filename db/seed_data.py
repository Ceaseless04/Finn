from server.app.utils.db import get_collection

def seed_data():
    users = get_collection("users")
    users.insert_many([
        {"email": "test@example.com", "name": "Test User", "password": "1234"},
        {"email": "test1@example.com", "name": "John Doe", "password": "12345678"},
    ])

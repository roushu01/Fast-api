from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
client=MongoClient(os.getenv("MONGO_URI"))
try:
    client.admin.command("ping")
    print("✅ MongoDB Connected Successfully")
except Exception as e:
    print("❌ MongoDB Connection Failed:", e)

db=client["test"]
user_collection=db["users"]

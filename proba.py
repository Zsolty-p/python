import os
from dotenv import load_dotenv

load_dotenv()

NAME=os.environ.get("name")

print(NAME)

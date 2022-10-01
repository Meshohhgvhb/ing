import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "9495729"))
API_HASH = getenv("API_HASH", "8a9aeb1762f724d591977b5dee4ad42c")
BOT_TOKEN = getenv("BOT_TOKEN", "5517070899:AAGzwArt8P4UjFVo3QsUogbD6qFZTN5ZYl0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BAB4kGvkmdzvxWnRUbOFkqVUrTe32jgNixfLgmoKv2sjOvrZjbqTr-VbgtyxqS0eEcUc3tN4qYXj-cUPybfGy7aJnNixZa65_-4ecFpwkvo193zf6KWZJA4Vgxaygmg49wN5FUVCK7yfQlBx5ZzcT7mi8rSevz8aPo6GrHg5CuCXy5Za3baYdtuLt96KR5u35G5XKZiM3nfdKziFf8Uyee7J-YuahLPNvbr83rRMTY_O6J5XjyYGWNHl6Dz27FNoxc6egOmV3UfZHeICpKgiY8_3Mp9E1BMALGspb7szm9L3nqZ3DuvzwZbYJwHi8E5jiZxSkm_20PPseOpl-I_3FPFwAAAAAVX1iBcA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", " ").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1923931101").split()))

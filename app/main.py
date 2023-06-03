from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from app.test.test import test_gets

load_dotenv()

app = FastAPI()

test_gets()

from dataclasses import dataclass
import os


@dataclass
class EmailUser:
    name: str
    email: str
    password: str


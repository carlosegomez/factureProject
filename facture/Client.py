from dataclasses import dataclass


@dataclass
class Client:
    name: str
    last_name: str
    phone: str
    address: str

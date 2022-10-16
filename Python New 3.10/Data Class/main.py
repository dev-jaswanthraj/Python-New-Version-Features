import random 
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k = 12))

@dataclass
class Person:
    name : str
    address : str
    active : str = True
    email_addresses: list[str] = field(default_factory = list)
    id : str = field(init = False, default_factory = generate_id)
   

def main() -> None:
    person = Person(name="Jaswanthraj", address="265-B Mullai Nagar", active=False)
    print(person)

if __name__ == "__main__":
    main()
import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile_number: str
    gender: str
    date_of_birth: str
    subjects: str
    hobbies: str
    address: str
    state: str
    city: str
    picture: str

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def state_and_city(self):
        return f"{self.state} {self.city}"



student = User(
    first_name="Anna",
    last_name="Kostina",
    email="111name@example.com",
    gender="Female",
    mobile_number="8788888888",
    date_of_birth='18 June,2025',
    subjects="Computer Science",
    hobbies="Reading",
    picture="duck.jpg",
    address="Moscow",
    state="Uttar Pradesh",
    city="Agra",
)
class Player:
    def __init__(self, name: str, position: str, age: int) -> None:
        self.name=name
        self.position=position
        self.age=age
    def __str__(self) -> str:
        return f"PLAYER INFO\nName: {self.name}\nAge: {self.age}\nPosition: {self.position}"
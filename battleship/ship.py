class Ship:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0

    def is_sunk(self) -> bool:
        return self.hits == self.size
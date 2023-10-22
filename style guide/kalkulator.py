class Kalkulator:
    # kalkulator tambah dan kurang
    def __init__(self, _i) -> None:
        self.i = _i

    def tambah(self, _i): return self.i + _i

    def kurang(self, _i):
        return self.i - _i

def usingInit():
    class Guest:
        def __init__(self, first, last, interest, phone):
            self.first = first
            self.last = last
            self.interest = interest
            self.phone = phone

    g_1 = Guest("Jayvee", "Mapote", "Anime", 2020161610)
    print(g_1.first)
usingInit()
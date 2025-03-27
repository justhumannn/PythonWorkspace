class Number:
    a: int
    def __mul__(self, obj):
        return self.a * obj.a
    def __init__(self, b):
        self.a = b

a = Number(1)
b = Number(2)

print(a*b)

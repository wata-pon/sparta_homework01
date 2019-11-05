"""
次のコードが正しく動作するような Rectangle クラスを実装してください
diagonal は 対角線(の長さ) という意味です。
rectangle1 = Rectangle(height=5, width=6)
rectangle1.area()  # 30.00
rectangle1.diagonal()  # 7.81

rectangle2 = Rectangle(height=3, width=3)
rectangle2.area()  # 9.00
rectangle2.diagonal()  # 4.24

area == w * h
diagonal == math.sqrt(h*h + w*w)
小数点第3位以下切り捨て
"""


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def diagonal(self):
        return math.sqrt(self.height ** 2 + self.width ** 2)


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())

rectangle2 = Rectangle(height=3, width=3)

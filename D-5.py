'''
counter1 = MyCounterV3(value=1, step=2)
print(counter1.value)  # 1
​
counter1.count_up()
print(counter1.value)  # 3
​
counter1.count_up()
print(counter1.value)  # 5
​
counter1.count_down()
print(counter1.value)  # 3
​
counter2 = MyCounterV3(value=3, step=4)
print(counter2.value)  # 3
​
counter2.count_down()
print(counter2.value)  # -1
​
counter2.count_down()
print(counter2.value)  # -5
以上


'''


class MyCounterV3:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step

    def count_down(self):
        self.value -= self.step


counter1 = MyCounterV3(1, 2)
print(counter1.value)

counter1.count_up()
print(counter1.value)

counter1.count_up()
print(counter1.value)

counter1.count_down()
print(counter1.value)

counter2 = MyCounterV3(3, 4)
print(counter2.value)

counter2.count_down()
print(counter2.value)

counter2.count_down()
print(counter2.value)

import pandas as pd
import matplotlib.pyplot as tino
class POINTS():
        def __init__(self, x, y):
            # self.x = my_point["x"]
            # self.y = my_point[" y"]
            self.x=x
            self.y=y
            print(self.x)
            plott = tino.scatter(self.x, self.y)
            plott_data = plt.show()
            return plott_data
        # def translate(self, dx, dy):
        #     self.x = self.x + dx
        #     self.y = self.y + dy

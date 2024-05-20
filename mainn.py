from CLASS import POINTS
import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv('coordinate_file.csv')
def plot_data(data):
    infor = data
    x = infor["x"]
    y = infor[" y"]
    translateX= 2
    translateY=2
    x1= x + translateX
    y1= y +translateY
    fig, ax = plt.subplots()
    colours=['blue','red']
    ax.scatter(x, y, c=colours[0])
    ax.scatter(x1, y1, c=colours[1])

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('combined Scatter plot')

    ax.legend()


    # print(x)
    # print(y)
    #plot = plt.scatter(x,y)
    return plt.show()
plot_data(file)


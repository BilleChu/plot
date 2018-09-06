import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
params = {'legend.fontsize': 22,
          'figure.figsize': (10, 10),
          'axes.labelsize': 25,
          'axes.titlesize':25,
          'xtick.labelsize':25,
          'ytick.labelsize':25}
pylab.rcParams.update(params)

colors = ['b', 'r', 'g', 'k']
linestyles = ['-', '-.']
labels = []

def read_data(file_path):
    with open(file_path, "r") as fread:
        return [float(i.strip()) for i in fread.readlines()]

def plot(data_lst):
    print (len(data_lst))
    for index, points in enumerate(data_lst):
        print (index)
        plt.plot(points,
                 color=colors[index%len(colors)],
                 linestyle=linestyles[index%len(linestyles)],
                 label=labels[index])
    plt.legend()
#    plt.ylabel()
#    plt.xlabel()
    plt.show()
    plt.savefig("img.jpg")


if __name__ == '__main__':
    file_lst= []
    for i in range(len(sys.argv)):
        if i > 0:
            filename=sys.argv[i]
            file_lst.append(read_data(filename))
            labels.append(filename)
    plot(file_lst)










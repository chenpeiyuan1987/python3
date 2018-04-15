import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(100000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6))

    size = list(range(rw.size))
    plt.scatter(rw.x_values(), rw.y_values(), c=size,
        cmap=plt.cm.rainbow, edgecolor='none', s=2)
    
    #plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    #plt.scatter(rw.x_values()[-1], rw.y_values()[-1], c='red',
    #    cmap=plt.cm.Blues, edgecolor='none', s=100)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break

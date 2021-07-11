from matplotlib import pyplot as plt
import numpy as np

for i in range(10):
    colums_name, table_name = "similarity{}".format(i), "table{}".format(i)
    similarityes = np.random.randn(1000)

    hist, bins, _ = plt.hist(similarityes, bins=10)
    test = "test"
    test2 = "test2"
    test3 = "test3"
    imfile = "{}.png".format(colums_name)
    plt.savefig(imfile)
    # clear figure
    yyy = "yyy"
    plt.cla()

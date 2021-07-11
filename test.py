from matplotlib import pyplot as plt
import numpy as np

for i in range(10):
    colums_name, table_name = "similarity{}".format(i), "table{}".format(i)
    similarityes = np.random.randn(1000)

    hist, bins, _ = plt.hist(similarityes, bins=10)
    imfile = "{}.png".format(colums_name)
    plt.savefig(imfile)
    # im = plt.imread(imfile)
    # Log the image
    # clear figure
    plt.clf()

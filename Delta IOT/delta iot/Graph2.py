import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter
while(True):
    topen = pd.read_csv("Temprature2.csv")
    lopen = pd.read_csv("Light2.csv")
    hopen = pd.read_csv("Humidity12.csv")


    plt.figure(1)

    plt.subplot(221)
    plt.plot(topen.values)
    plt.title('Temprature')
    plt.grid(True)


    plt.subplot(222)
    plt.plot(lopen.values)
    plt.title('Light')
    plt.grid(True)


    plt.subplot(223)
    plt.plot(hopen.values)
    plt.title('Humidity')
    plt.grid(True)


    plt.gca().yaxis.set_minor_formatter(NullFormatter())
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)

    plt.show()
    print("All done")
    time.sleep(10)



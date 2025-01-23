import numpy as np
import matplotlib.pyplot as plt


def draw_scatter_plot():

    np.random.seed(123)

    x = np.arange(10)
    y = np.random.rand(10) * 10

    fig, ax = plt.subplots()

    ax.scatter(x, y, color='blue', label='Random Points', alpha=0.7)

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title('Scatter Plot Example')
    ax.legend()

    return fig


if __name__ == '__main__':
    fig = draw_scatter_plot()
    plt.show()

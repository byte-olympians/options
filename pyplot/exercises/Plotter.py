# Add these two lines
import matplotlib
matplotlib.use('Agg')
###
import matplotlib.pyplot as plt

class Plotter:
    """Uses pyplot to plot out various graphs"""

    def __init__(self):
        pass

    def plot_single_line(self):
        plt.plot([1,2,3,4])
        plt.ylabel('some numbers')
        ### use plt.savefig instead of plt.show().The graph will be saved in test.jpg
        plt.savefig('test.jpg')

    def plot_multi_line(self):
        x_axis = range(0, 10)
        plt.plot(x_axis, [0,1,2,3,4,5,6,7,8,9], label='Line 1')
        plt.plot(x_axis, [9,8,7,6,5,4,3,2,1,0], label='Line 2')
        plt.plot(x_axis, [0,2,4,6,8,10,12,14,16,18], label='Line 3')
        plt.legend(loc=0)
        plt.xlabel('Samples')
        plt.ylabel('Values')
        plt.title('Sampling Results')
        plt.annotate('Point of Interest', xy=(9,9), xytext=(6,9), arrowprops=dict(facecolor='black', shrink=0.5))
        plt.savefig('multiplelines.jpg')

    def plot_pie(self):
        voting_results = {
            'Trump': 25, 'Rubio': 19, 'Cruz': 30, 'Bush': 29, 'Christie': 20}
        plt.pie([voting_results['Trump'],voting_results['Rubio'],voting_results['Bush'],voting_results['Christie']])
        plt.savefig('pie.jpg')


# Runner
plotter = Plotter()
plotter.plot_single_line()
plotter.plot_multi_line()
plotter.plot_pie()

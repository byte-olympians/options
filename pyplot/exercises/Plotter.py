
class Plotter(object):
    """Uses pyplot to plot out various graphs"""

    def __init__(self, arg):
        super(Plotter, self).__init__()

    def plot_single_line(self):
        pass

    def plot_multi_line(self):
        pass

    def plot_pie(self):
        voting_results = {
            'Trump': 25, 'Rubio': 19, 'Cruz': 30, 'Bush': 29, 'Christie': 20}


# Runner
plotter = Plotter()
plotter.plot_single_line()
plotter.plot_multi_line()
plotter.plot_pie()

import plotting

class Beagle(object):
    default_plot_functions = [
        plotting.scatter_plotter
    ]
    def __init__(self, dataset):
        self.dataset = dataset

    def generate(self):
        pass
import plotting


class Beagle(object):
    default_plot_functions = [
        plotting.scatter_plotter
    ]

    def __init__(self, dataset):
        self.dataset = dataset
        self.column_meta = self.generate_column_meta()

    def generate_column_meta(self):
        """Returns metadata used by determine applicableness of plots"""
        meta = {}
        for column_name in list(self.dataset):
            n_unique = self.dataset[column_name].nunique()
            probable_type = 'Unknown'
            if n_unique == 2:
                probable_type = 'Binary'
            elif 2 < n_unique < 10:
                probable_type = 'Category'
            elif n_unique >= 10:
                probable_type = 'Continuous'

            meta[column_name] = {'probable_type': probable_type}

        return meta

    def generate(self):
        # columns by themselves
        pass
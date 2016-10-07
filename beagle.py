import plotting


class Beagle(object):
    default_plot_classes = [
        plotting.ScatterPlotter
    ]

    def __init__(self, dataset):
        """For now assumes dataset to be a pandas dataframe"""
        self.dataset = dataset
        self.column_names = list(self.dataset)
        self.column_meta = self.generate_column_meta()

        self.base_dir = "./"
        self.base_figsize = (6, 4.5)
        self.file_num = 0

    def generate_column_meta(self):
        """Returns metadata used by determine applicableness of plots"""
        meta = {}
        for column_name in self.column_names:
            n_unique = self.dataset[column_name].nunique()
            probable_type = 'Unknown'
            if n_unique == 2:
                probable_type = 'Binary'
            elif 2 < n_unique < 10:
                probable_type = 'Category'
            elif n_unique >= 10:
                probable_type = 'Continuous'

            meta[column_name] = {'probable_type': probable_type,
                                 'n_unique': n_unique}

        return meta

    def start_exploring(self):
        for column_name in self.column_names:
            self.generate_appropriate_plots([column_name], 2)

    def dive_deeper_into(self, topic):
        pass

    def generate_appropriate_plots(self, columns, threshold):
        """For one or multiple columns of data, generates plots above threshold"""
        file_nums_used = set()
        for plot_class in self.default_plot_classes:
            score, reason = plot_class.appropriate_score(
                columns, self.dataset, self.column_meta)

            if score >= threshold:
                filename = self.base_dir + str(self.file_num) + '.png'
                file_nums_used.add(self.file_num)
                self.file_num += 1

                pc = plot_class(self.base_figsize)
                pc.generate_plot(self.dataset, filename)

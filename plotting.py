class PlotterMetaclass(object):
    def __init__(self, figsize):
        self.figsize = figsize


class ScatterPlotter(PlotterMetaclass):
    @staticmethod
    def appropriate_score(column_names, dataset, dataset_meta):
        """Returns a score for appropriateness of this plot, plus explanation"""
        return 0, 'Not Implemented yet'

    def generate_plot(self, data, filename):
        pass

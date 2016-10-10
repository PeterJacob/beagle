import plotting


class Beagle(object):
    default_plot_classes = [
        plotting.SimpleCountPlot,
        plotting.OneDimKernelEstimationPlot,
        plotting.TwoDimKernelEstimationPlot,
        plotting.SimpleScatterPlot,
        plotting.ColoredScatterPlot,
        plotting.SimpleBoxPlot,
        plotting.SimpleSwarmPlot,
        plotting.SimpleViolinPlot,
        plotting.SimpleMosaicPlot
    ]

    def __init__(self, dataset, base_dir='./out/'):
        """Interactive data exploration tool
        
        Args:
            dataset (DataFrame): Data to perform exploration on. For now
                assumes dataset to be a Pandas dataframe. May do duck-typing
                later.
            base_dir (str): Location to write generated content to.
                Terminate with a slash.
        """
        self.dataset = dataset
        self.base_dir = base_dir
        
        self.column_names = list(self.dataset)
        self.column_meta = self.generate_column_meta()

        self.base_figsize = (6, 4.5)
        self.file_num = 0

    def generate_column_meta(self):
        """Returns metadata used to determine applicableness of plots"""
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
        """Write files required to explore to disk"""
        # One dimension
        file_nums_used = []
        for column_name in self.column_names:
            used = self.generate_appropriate_plots([column_name], 2)
            file_nums_used += used
        
        filename = self.base_dir + 'index.html'
        self.generate_html(filename, file_nums_used)
        
        # One dimension detail + two dimensions
        for i1, column_name1 in enumerate(self.column_names):
            file_nums_used = []
            used = self.generate_appropriate_plots([column_name1], 1)
            file_nums_used += used
            for i2, column_name2 in enumerate(self.column_names):
                if i2 == i1:
                    continue  # Do not cross with self
                column_names = [column_name1, column_name2]
                used = self.generate_appropriate_plots(column_names, 2)
                file_nums_used += used
        
            filename = self.base_dir + column_name1 + '.html'
            self.generate_html(filename, file_nums_used)
        
        # Two dimention detail
        for i1, column_name1 in enumerate(self.column_names):
            for i2, column_name2 in enumerate(self.column_names):
                if i2 == i1:
                    continue  # Do not cross with self

                column_names = [column_name1, column_name2]
                file_nums_used = self.generate_appropriate_plots(column_names, 1)

                filename = '{}{}-{}.html'.format(
                    self.base_dir, column_name1, column_name2)
                self.generate_html(filename, file_nums_used)
    
    def generate_html(self, html_filename, fig_info):
        header = "<html><body>"
        footer = "</body></html>"
        middle_template = '<p><a href="{}"><img src="{}" /></a></p>'
        middle = ""
        for filenum, columns in list(fig_info):
            link_filename = '-'.join(columns) + '.html'
            fig_filename = str(filenum) + '.png'
            middle += middle_template.format(link_filename, fig_filename)
        
        with open(html_filename, 'w') as f:
            f.write(header + middle + footer)

    def generate_appropriate_plots(self, columns, threshold):
        """For one or multiple columns, generates plots above threshold"""
        file_nums_used = []
        for plot_class in self.default_plot_classes:
            score = plot_class.appropriate_score(
                columns, self.dataset, self.column_meta)

            if score >= threshold:
                filename = self.base_dir + str(self.file_num) + '.png'
                file_nums_used.append((self.file_num, columns))
                self.file_num += 1

                plot_class.generate_plot(
                    columns, self.dataset, self.column_meta,
                    filename, self.base_figsize)
        return file_nums_used

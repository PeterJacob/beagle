import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic


class SimpleCountPlot(object):
    @staticmethod
    def appropriate_score(column_names, dataset, dataset_meta):
        """Returns a score for appropriateness of a simple count plot"""
        probable_type = dataset_meta[column_names[0]]['probable_type']
        if (len(column_names) == 1 and
            (probable_type == 'Category' or probable_type == 'Binary')):
            return 2  # Very appropriate
        else:
            return 0  # Not appropriate

    @staticmethod
    def generate_plot(column_names, dataset, dataset_meta, 
                      filename, figsize=(6, 4.5)):
        plt.figure(figsize=figsize)
        sns.countplot(dataset[column_names[0]])
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()


class SimpleDistPlot(object):
    @staticmethod
    def appropriate_score(column_names, dataset, dataset_meta):
        """Returns a score for appropriateness of a simple dist plot"""
        if (len(column_names) == 1 and
            dataset_meta[column_names[0]]['probable_type'] == 'Continuous'):
            return 2  # Very appropriate
        else:
            return 0  # Not appropriate

    @staticmethod
    def generate_plot(column_names, dataset, dataset_meta, 
                      filename, figsize=(6, 4.5)):
        plt.figure(figsize=figsize)
        sns.distplot(dataset[column_names[0]], hist=False, rug=True)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()


class SimpleScatterPlot(object):
    @staticmethod
    def appropriate_score(column_names, dataset, dataset_meta):
        """Returns a score for appropriateness of a simple scatter plot"""
        probable_types = [dataset_meta[column_name]['probable_type'] 
                          for column_name in column_names]
        if (len(column_names) == 2 and
            probable_types == ['Continuous', 'Continuous']):
            return 2  # Very appropriate
        else:
            return 0  # Not appropriate

    @staticmethod
    def generate_plot(column_names, dataset, dataset_meta, 
                      filename, figsize=(6, 4.5)):
        plt.figure(figsize=figsize)
        plt.scatter(dataset[column_names[0]],
                    dataset[column_names[1]])
        plt.xlabel(column_names[0])
        plt.ylabel(column_names[1])
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()


class SimpleBoxPlot(object):
    @staticmethod
    def appropriate_score(column_names, dataset, dataset_meta):
        """Returns a score for appropriateness of a simple box plot"""
        probable_types = [dataset_meta[column_name]['probable_type'] 
                          for column_name in column_names]
        if (len(column_names) == 2 and
            (sorted(probable_types) == ['Categorical', 'Continuous'] or
             sorted(probable_types) == ['Binary', 'Continuous'])):
            return 2  # Very appropriate
        else:
            return 0  # Not appropriate

    @staticmethod
    def generate_plot(column_names, dataset, dataset_meta, 
                      filename, figsize=(6, 4.5)):
        if dataset_meta[column_names[0]]['probable_type'] == 'Continuous':
            continuous_column_name = column_names[0]
            other_column_name = column_names[1]
        else:
            continuous_column_name = column_names[1]
            other_column_name = column_names[0]
            
        plt.figure(figsize=figsize)
        sns.boxplot(x=other_column_name,
                    y=continuous_column_name,
                    data=dataset)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()


class SimpleMosaicPlot(object):
    @staticmethod
    def appropriate_score(column_names, dataset, dataset_meta):
        """Returns a score for appropriateness of a simple mosaic plot"""
        probable_types = [dataset_meta[column_name]['probable_type'] 
                          for column_name in column_names]
        if (len(column_names) == 2 and
            (sorted(probable_types) == ['Category', 'Category'] or
             sorted(probable_types) == ['Binary', 'Category'] or
             sorted(probable_types) == ['Binary', 'Binary'])):
            return 2  # Very appropriate
        else:
            return 0  # Not appropriate

    @staticmethod
    def generate_plot(column_names, dataset, dataset_meta, 
                      filename, figsize=(6, 4.5)):
#        if dataset_meta[column_names[0]]['probable_type'] == 'Binary':
        first_column_name = column_names[0]
        second_column_name = column_names[1]
#        else:
#            first_column_name = column_names[1]
#            second_column_name = column_names[0]
            
        plt.figure(figsize=figsize)
        title = "Horizontal: " + first_column_name +\
                ", Vertical: " + second_column_name
        mosaic(dataset,
               [first_column_name, second_column_name],
               ax=plt.gca(),
               gap=0.01,
               title=title)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

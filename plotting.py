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


class CategoryCountPlot(object):
    @staticmethod
    def appropriate_score(column_names, dataset, dataset_meta):
        """Returns a score for appropriateness of a category count plot"""
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
        plt.figure(figsize=figsize)
        sns.countplot(x=column_names[0], hue=column_names[1], data=dataset)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()


class OneDimKernelEstimationPlot(object):
    @staticmethod
    def appropriate_score(column_names, dataset, dataset_meta):
        """Returns a score for appropriateness of a 1d kernel density plot"""
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


class TwoDimKernelEstimationPlot(object):
    @staticmethod
    def appropriate_score(column_names, dataset, dataset_meta):
        """Returns a score for appropriateness of a 2d kernel denstiy plot"""
        probable_types = [dataset_meta[column_name]['probable_type'] 
                          for column_name in column_names]
        if (len(column_names) == 2 and
            probable_types == ['Continuous', 'Continuous']):
            return 1  # Moderately appropriate
        else:
            return 0  # Not appropriate

    @staticmethod
    def generate_plot(column_names, dataset, dataset_meta, 
                      filename, figsize=(6, 4.5)):
        plt.figure(figsize=figsize)
        sns.kdeplot(dataset[column_names[0]], dataset[column_names[1]])
        plt.xlabel(column_names[0])
        plt.ylabel(column_names[1])
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
        sns.lmplot(x=column_names[0],
                   y=column_names[1],
                   data=dataset,
                   fit_reg=False,
                   scatter_kws={'alpha': 0.5}) # Maybe auto-adjust later
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()


class ColoredScatterPlot(object):
    @staticmethod
    def appropriate_score(column_names, dataset, dataset_meta):
        """Returns a score for appropriateness of a colored scatter plot"""
        probable_types = [dataset_meta[column_name]['probable_type'] 
                          for column_name in column_names]
                          
        allowed_probable_types = [['Binary', 'Continuous', 'Continuous'],
                                  ['Continuous', 'Continuous', 'Category']]
                                  
        if sorted(probable_types) in allowed_probable_types:
            return 2  # Very appropriate
        else:
            return 0  # Not appropriate

    @staticmethod
    def generate_plot(column_names, dataset, dataset_meta, 
                      filename, figsize=(6, 4.5)):
        probable_types = [dataset_meta[column_name]['probable_type'] 
                          for column_name in column_names]

        if probable_types[0] != 'Continuous':
            x_idx, y_idx, hue_idx = 1, 2, 0
        elif probable_types[1] != 'Continuous':
            x_idx, y_idx, hue_idx = 0, 2, 1
        else:
            x_idx, y_idx, hue_idx = 0, 1, 2
            
        plt.figure(figsize=figsize)
        sns.lmplot(x=column_names[x_idx],
                   y=column_names[y_idx],
                   hue=column_names[hue_idx],
                   data=dataset,
                   fit_reg=False,
                   scatter_kws={'alpha': 0.3}) # Maybe auto-adjust later
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
            (sorted(probable_types) == ['Category', 'Continuous'] or
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


class SimpleSwarmPlot(object):
    @staticmethod
    def appropriate_score(column_names, dataset, dataset_meta):
        """Returns a score for appropriateness of a simple swarm plot"""
        probable_types = [dataset_meta[column_name]['probable_type'] 
                          for column_name in column_names]

        if (len(column_names) == 2 and
            (sorted(probable_types) == ['Category', 'Continuous'] or
             sorted(probable_types) == ['Binary', 'Continuous'])):
            return 1  # Moderately appropriate
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
        sns.swarmplot(x=other_column_name,
                      y=continuous_column_name,
                      data=dataset)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()


class SimpleViolinPlot(object):
    @staticmethod
    def appropriate_score(column_names, dataset, dataset_meta):
        """Returns a score for appropriateness of a simple violin plot"""
        probable_types = [dataset_meta[column_name]['probable_type'] 
                          for column_name in column_names]

        if (len(column_names) == 2 and
            (sorted(probable_types) == ['Category', 'Continuous'] or
             sorted(probable_types) == ['Binary', 'Continuous'])):
            return 1  # Moderately appropriate
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
        sns.violinplot(x=other_column_name,
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
            return 1  # Moderately appropriate
        else:
            return 0  # Not appropriate

    @staticmethod
    def generate_plot(column_names, dataset, dataset_meta, 
                      filename, figsize=(6, 4.5)):

        first_column_name = column_names[0]
        second_column_name = column_names[1]
            
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

all_plot_classes = [
    SimpleCountPlot,
    CategoryCountPlot,
    OneDimKernelEstimationPlot,
    TwoDimKernelEstimationPlot,
    SimpleScatterPlot,
    ColoredScatterPlot,
    SimpleBoxPlot,
    SimpleSwarmPlot,
    SimpleViolinPlot,
    SimpleMosaicPlot
]
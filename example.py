from pydataset import data
from beagle import Beagle

dataset = data('iris')
b = Beagle(dataset, base_dir='./out/')

b.start_exploring()

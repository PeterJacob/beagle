from pydataset import data
from beagle import Beagle

dataset = data('titanic')
b = Beagle(dataset)

b.start_exploring()
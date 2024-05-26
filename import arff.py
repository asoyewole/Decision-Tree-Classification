import arff
import pandas as pd


data = arff.load(open('phpMYEkMl.arff', 'r'))
data = pd.DataFrame(data['data'])
print(data.head())
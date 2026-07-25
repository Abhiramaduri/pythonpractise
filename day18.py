#Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
#ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

#print('Count:', data.count()) # 25
#print('Sum: ', data.sum()) # 744
#print('Min: ', data.min()) # 24
#print('Max: ', data.max()) # 38
#print('Range: ', data.range()) # 14
#print('Mean: ', data.mean()) # 30
#print('Median: ', data.median()) # 29
#print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
#print('Standard Deviation: ', data.std()) # 4.2
#print('Variance: ', data.var()) # 17.5
#print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
# you output should look like this
#print(data.describe())
#Count: 25
#Sum:  744
#Min:  24
#Max:  38
#Range:  14
#Mean:  30
#Median:  29
#Mode:  (26, 5)
#Variance:  17.5
#Standard Deviation:  4.2
#Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

from collections import Counter
from statistics import mean, median, mode
import math


class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(sum(self.data) / len(self.data), 2)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return round((sorted_data[mid - 1] + sorted_data[mid]) / 2, 2)
        return sorted_data[mid]

    def mode(self):
        counts = Counter(self.data)
        max_count = max(counts.values())
        modes = [value for value, count in counts.items() if count == max_count]
        return (modes[0], max_count)

    def std(self):
        avg = self.mean()
        variance = sum((x - avg) ** 2 for x in self.data) / (len(self.data) - 1)
        return round(math.sqrt(variance), 2)

    def var(self):
        avg = self.mean()
        return round(sum((x - avg) ** 2 for x in self.data) / (len(self.data) - 1), 2)

    def freq_dist(self):
        counts = Counter(self.data)
        total = len(self.data)
        return [(round(count / total * 100, 2), value) for value, count in sorted(counts.items())]

    def describe(self):
        return f"Count: {self.count()}\nSum:  {self.sum()}\nMin:  {self.min()}\nMax:  {self.max()}\nRange:  {self.range()}\nMean:  {self.mean()}\nMedian:  {self.median()}\nMode:  {self.mode()}\nVariance:  {self.var()}\nStandard Deviation:  {self.std()}\nFrequency Distribution: {self.freq_dist()}"


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode())
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())
print('Frequency Distribution: ', data.freq_dist())
print(data.describe())

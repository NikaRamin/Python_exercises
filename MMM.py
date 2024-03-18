"""
Mean - The average value
Median - The mid point value
Mode - The most common value
"""
import numpy
from scipy import stats
grades = [2, 5, 16, 27, 1, 19, 20, 4, 0, 1, 2, 15, 13, 11, 12, 9, 6, 11, 11]
mean_grades = numpy.mean(grades)
median_grades = numpy.median(grades)
mode_result = stats.mode(grades)
mode_grades = mode_result.mode  # Extracting the mode from the result
mode_count = mode_result.count  # Extracting the count of the mode

print("Mean:", "{:.4f}".format(mean_grades))
print("Median:", median_grades)
print("Mode:", mode_grades, "(Count:",mode_count,")")

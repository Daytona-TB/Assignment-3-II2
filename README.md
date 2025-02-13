# Assignment-3-II2

**Iris Species Analysis**

**Project Overview**
This project analyzes the Fisher Iris dataset by computing statistical measures and comparing species similarity based on their petal and sepal dimensions.

**Implementation Details**
Merges petal and sepal datasets into a single DataFrame.
Computes correlations, averages, medians, and standard deviations for each species.
Determines species similarity using Euclidean distance.

**Class & Method Explanation**
merge_datasets(petal_data, sepal_data): Combines datasets on sample_id and species.
calculate_statistics(df): Computes mean, median, and standard deviation for each species.
compute_similarity(df): Uses Euclidean distance to determine species similarity.

**Limitations**
No missing data handling: Assumes all values are correctly formatted.
Euclidean distance limitation: Does not account for outliers or distributions beyond mean differences.

**Results Summary**
Most Similar Species: Versicolor and Virginica (Euclidean Distance: 1.429)
Least Similar Species: Setosa and Virginica (Euclidean Distance: 4.581)

**Justification**
The similarity is determined using Euclidean distance, which measures the overall difference in mean petal and sepal dimensions. A smaller distance indicates closer similarity.
Versicolor and Virginica have the smallest distance, meaning they share more similar petal and sepal measurements.
Setosa and Virginica have the largest distance, showing the most significant differences in their physical traits.

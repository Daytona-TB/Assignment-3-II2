import pandas as pd

# File paths
petal_data_path = "/Users/lucashandlon/Desktop/I.I. 2/Petal_Data.csv"
sepal_data_path = "/Users/lucashandlon/Desktop/I.I. 2/Sepal_Data.csv"

# Load the data
petal_data = pd.read_csv(petal_data_path).drop(columns=['Unnamed: 0'])
sepal_data = pd.read_csv(sepal_data_path).drop(columns=['Unnamed: 0'])

# Merge the datasets on 'sample_id' and 'species'
iris_data = pd.merge(petal_data, sepal_data, on=['sample_id', 'species'])

# Calculate correlations between variables
correlations = iris_data[['petal_length', 'petal_width', 'sepal_length', 'sepal_width']].corr()
print("Correlations:\n", correlations)

# Calculate averages for each variable
averages = iris_data.groupby('species').mean(numeric_only=True)
print("\nAverages:\n", averages)

# Calculate medians for each variable
medians = iris_data.groupby('species').median(numeric_only=True)
print("\nMedians:\n", medians)

# Calculate standard deviations for each variable
std_devs = iris_data.groupby('species').std(numeric_only=True)
print("\nStandard Deviations:\n", std_devs)

# Compute Euclidean distance using only Pandas
def euclidean_distance(df, species1, species2):
    return ((df.loc[species1] - df.loc[species2]) ** 2).sum() ** 0.5

# Compute distances between species
distance_setosa_versicolor = euclidean_distance(averages, "setosa", "versicolor")
distance_setosa_virginica = euclidean_distance(averages, "setosa", "virginica")
distance_versicolor_virginica = euclidean_distance(averages, "versicolor", "virginica")

# Store results in a DataFrame
similarity_results = pd.DataFrame({
    "Species Comparison": ["Setosa vs Versicolor", "Setosa vs Virginica", "Versicolor vs Virginica"],
    "Euclidean Distance": [distance_setosa_versicolor, distance_setosa_virginica, distance_versicolor_virginica]
})

print("\nSpecies Similarity Analysis:\n", similarity_results)

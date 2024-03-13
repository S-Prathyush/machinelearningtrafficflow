# Load the dataset
df = pd.read_csv('AccidentReports.csv')

# Print column names to check for leading or trailing spaces
print(df.columns)

# Split features and target variable
X = df.drop('Accident_Location', axis=1)  # Use exact column name from DataFrame
y = df['Accident_Location']                # Use exact column name from DataFrame

# Convert y to string to avoid mix of string and float data types
y = y.astype(str)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline and model training...

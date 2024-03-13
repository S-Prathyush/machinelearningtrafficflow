import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('AccidentReports.csv', encoding='latin1')  # Replace 'your_dataset.csv' with the path to your dataset file

# Preprocess the data
# Remove rows with missing values in the 'Accident_Location' column
data.dropna(subset=['Accident_Location'], inplace=True)

# Split the dataset into features (X) and the target variable (y)
X = data['Accident_Location']  # Features
y = data['Accident_Spot']     # Target variable (e.g., 'Accident_Classification')

# Convert text data to numerical features using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Visualize the relationship between 'Accident_Location' and 'Accident_Spot'
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Accident_Location', hue='Accident_Spot')
plt.xticks(rotation=45)
plt.title('Accident Spot Distribution by Location')
plt.xlabel('Accident Location')
plt.ylabel('Count')
plt.legend(title='Accident Spot')
plt.tight_layout()
plt.show()
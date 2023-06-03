import pickle
import pandas as pd
import sqlite3
from sklearn.preprocessing import StandardScaler


# Load the trained model
with open('best_nn_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the samples to classify
samples = pd.read_csv('data/df_test.csv')


# Scale the input variables
scaler = StandardScaler()
samples_scaled = scaler.fit_transform(samples)

# Make predictions
predictions = model.predict(samples_scaled)

# Store the results in a SQLite database table
conn = sqlite3.connect('data/predictions_test.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS predictions (id INTEGER PRIMARY KEY, class TEXT)''')

# Insert the predictions into the table
for i, pred in enumerate(predictions):
    c.execute("INSERT INTO predictions (id, class) VALUES (?, ?)", (i, pred))

# Commit the changes and close the connection
conn.commit()
conn.close()

conn = sqlite3.connect('data/predictions_test.db')
df = pd.read_sql_query("SELECT * FROM predictions", conn)
conn.close()

print(df)
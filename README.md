# Weather prediction classification ☀️🌥️🌧️❄️

In this repository I try different classification algorithems to classify the weather conditions of Istanbul. 

Hand Guide:

1. Ensure you have the required dependencies installed. You can install them using pip if you haven't already:


```
pip install pandas scikit-learn sqlite3
```

2. Make sure you have the following files in the same directory as the .py script:

- The trained model file: `best_nn_model.pkl`
- The input file containing samples to classify: `data/df_test.csv`

3. Run the .py script using the command line or your preferred Python IDE. If you are using the command line, navigate to the directory containing the script and run the following command:

```
python script_name.py
```

Replace `script_name.py` with the actual name of your .py script.

4. After running the script, a new SQLite database file named `predictions_test.db` will be created in the `data` directory. This database contains a table called `predictions`, which stores the classification results with fields `id` and `class`.

5. To view the contents of the `predictions` table, you can use an SQLite database viewer or run the following Python code:

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('data/predictions_test.db')
df = pd.read_sql_query("SELECT * FROM predictions", conn)
conn.close()

print(df)
```

This code will print the contents of the `predictions` table as a pandas DataFrame.

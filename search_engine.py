import sqlite3
import pandas as pd
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# 1. Load Data
try:
    conn = sqlite3.connect("faculty.db")
    df = pd.read_sql_query("SELECT * FROM faculty", conn)
    conn.close()
    print(f"✅ Loaded {len(df)} faculty members from SQLite.")
except Exception as e:
    print(f"❌ Database Error: {e}")
    exit()

# 2. Prepare the "Context" (Rich Text for AI)
# We combine everything so the search is highly accurate
df['combined_text'] = (
    "Name: " + df['Name'].fillna('') + ". " +
    "Specialization: " + df['Specialization'].fillna('') + ". " +
    "Research: " + df['Research_Interests'].fillna('') + ". " +
    "Teaching: " + df['Teaching'].fillna('') + ". " +
    "Pubs: " + df['Publications'].fillna('')
)

# 3. Load Model & Generate Embeddings
print("🚀 Loading Model (all-MiniLM-L6-v2)...")
model = SentenceTransformer('all-MiniLM-L6-v2')

print("🧠 Generating Embeddings... This may take a minute.")
# Ensure we convert to a standard NumPy array for the backend
embeddings = model.encode(df['combined_text'].tolist(), show_progress_bar=True)
embeddings = np.array(embeddings).astype('float32') 

# 4. Save
try:
    with open("faculty_data.pkl", "wb") as f:
        # Saving as a dictionary so main.py can easily extract them
        pickle.dump({'dataframe': df, 'embeddings': embeddings}, f)
    print(f"✅ SUCCESS: 'faculty_data.pkl' created. Size: {embeddings.shape}")
except Exception as e:
    print(f"❌ Save Error: {e}")


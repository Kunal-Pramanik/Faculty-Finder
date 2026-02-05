import pandas as pd
import re

df = pd.read_csv("daiictfaculty.csv")
df.columns = df.columns.str.strip()

def clean_text(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

df["Research_area"] = df["Research_area"].apply(clean_text)


#  DROP EMPTY ROWS
df = df[df["Research_area"] != ""]

# DROP DUPLICATE ROWS BASED ON CLEANED TEXT
df = df.reset_index(drop=True)

# ADD FACULTY ID
df.insert(0, "faculty_id", [f"F-{str(i+1).zfill(2)}" for i in range(len(df))])

df.to_csv("dau_faculty.csv", index=False)

print("Remaining rows:", len(df))

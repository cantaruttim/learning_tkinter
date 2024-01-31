from tkinter.filedialog import askopenfilename
import pandas as pd

file_path = askopenfilename(title="Select an file to open")

df = pd.read_excel(file_path)

print(df)


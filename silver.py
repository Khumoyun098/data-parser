"""
    Read text data
"""

# Extract words from content

import pandas as pd

df = pd.read_csv('main.csv', usecols=['source_url', 'access_datetime', 'content'])

contents_to_words = df["content"].str.split(" ")

result = []

for content in contents_to_words:
    result.append(list(filter(None, content)))

df['words'] = result
df['count'] = [len(x) for x in result]

df.to_csv('main.csv', encoding='utf-8')

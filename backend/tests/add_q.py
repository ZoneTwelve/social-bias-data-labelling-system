#!/usr/bin/env python
import requests
import json

url = 'http://127.0.0.1:5000/api/question'  # Replace with the actual URL of your API

def send(data):
    """
    data = {
        'biased_sentence': 'This is a sample biased sentence.',
        'tac': 'some_tac_value',  # Optional
        'source': 'some_source',  # Optional
        'identity': 'some_identity'  # Optional
    }
    """

    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 201:
        print('Question added successfully!')
        print(response.json())  # Print the response
    else:
        print('Error:', response.status_code)
        print(response.text)

if __name__ == "__main__":
    import sys
    import pandas as pd
    data = pd.read_csv(sys.argv[1])

    for index in range(len(data)):
        row = data.iloc[index]  # Access row by index

        # Assuming your CSV columns match the 'data' dictionary keys
        question_data = {
            # Sentence ID,Biased Sentences,T-A Combination,Source,Identity,是否有偏見 (有1 沒有 0 不確定-1),是否有惡意言論 (有1 沒有 0 不確定-1)
            'sentence_id': int(row['Sentence ID']),
            'biased_sentence': row['Biased Sentences'],
            'tac': row.get('T-A Combination'),  # Handle potential missing 'tac' column
            'source': row.get('Source'),
            'identity': row.get('Identity')
        }

        send(question_data)  # Send the constructed data

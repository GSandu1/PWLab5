import pickle

# Sample data
data = {'key': 'value', 'number': 42}

# Pickle the dictionary to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

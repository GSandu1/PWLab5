import pickle

data = {'key': 'value', 'number': 42}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

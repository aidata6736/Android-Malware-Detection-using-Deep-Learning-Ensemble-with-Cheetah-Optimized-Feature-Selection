import os
import pickle


def save(name, val):
    # Create the directory if it doesn't exist
    if not os.path.exists('./Saved data/'):
        os.makedirs('./Saved data/')

    # Save the data into the specified file using pickle
    with open('./Saved data/'+name+'.pkl', "wb") as file:
        pickle.dump(val, file)

def load(name):
    # Open the file in binary mode
    with open("./Saved data/" + name + '.pkl', "rb") as file:
        # Call load method to deserialze
        myvar = pickle.load(file)
    return myvar


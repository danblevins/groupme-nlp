import pandas as pd

def get_nicknames(data):
    nicknames = []

    for name in data['name'].unique():
        subset = data[data.name == name]
        my_nicknames = list(subset.nickname.unique())
        my_nicknames = ["@" + s for s in my_nicknames]
        nicknames.append(my_nicknames)
    
    lengths = [len(i) for i in nicknames]
    nicknames_df = pd.DataFrame({'length': lengths, 'name': data["name"].unique()})

    return nicknames_df
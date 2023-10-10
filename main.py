from GO import GoGame

import pandas as pd
import csv

game = GoGame() 




def data_clean():
    data = []
    with open("data_set\dan_train.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    # Convert the list of lists to a DataFrame
    df = pd.DataFrame(data)
  
    df = df.drop([0, 1], axis=1)

   
    return df



    
def convert_to_tuple(index_list):
    # Extract characters inside the brackets
    game_state = []

    for s in index_list:
        chars = s[2:-1]
        
        # Convert each character to its index in the alphabet
        tmp = tuple(ord(c) - ord('a') for c in chars)
        if tmp not in game_state:
            game_state.append(tmp)
    
    return game_state


def select_rows(data,index):
    row_data = data.iloc[[0]]
    index_list = []
    for column in row_data:
        for index in row_data[column]:
            if index !=None:
                index_list.append(index)
    return index_list          




if __name__ == "__main__":
    data = data_clean()
    row_index = convert_to_tuple(select_rows(data,0))



    while True:
        for index, move in enumerate(row_index):
            color = 'black' if index % 2 == 0 else 'white'
            state = game.step(move, color)






   

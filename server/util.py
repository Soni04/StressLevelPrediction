import pickle
import json
import numpy as np


__data_columns=None
__model=None

def get_stressLevel(humidity,temperature,step_count):
    global __model
    global __data_columns
    if __model is None:
        load_saved_artifacts()
    x = np.zeros(len(__data_columns))
    x[0] = humidity
    x[1] = temperature
    x[2] = step_count

    return int(__model.predict([x])[0])


def load_saved_artifacts():
    print("loading saved artifacts")
    global __data_columns
    
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        
    global __model
    if __model is None:
        with open ("./artifacts/stress_prediction.pickle",'rb')as f:
            __model=pickle.load(f)
            print("loading saved artifacts ...done")
            
def get_data_columns():
    return __data_columns
        
if __name__ =='__main__':
    load_saved_artifacts()
    print(get_stressLevel(27,97,196))
    
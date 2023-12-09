import re

def get_prediction_value(history):
    placeholder : int =0
    history[-1].insert(0,placeholder)
    for index in range(len(history),1,-1):
        placeholder = history[index-2][0] - history[index-1][0]
        history[index-2].insert(0,placeholder)
    #print(history)
    return placeholder

def check_all_zeros(steps):
    for step in steps:
        if step != 0:
            return True
    return False

def get_place_holder(series):
    history = []
    history.append(series)
    while check_all_zeros(series):
        new_series = []
        for index in range(len(series)-1):
            new_series.append(series[index+1] - series[index])
        series = new_series
        history.append(series)
    return history

with open('input.txt','r') as f:
    lines = f.read().splitlines()

plceholder = []
for line in lines:
    series = list(map(int, re.findall(r"-?\d+", line)))
    plceholder.append(get_prediction_value(get_place_holder(series)))
print(sum(plceholder))
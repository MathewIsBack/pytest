def get_average():
    with open('num.txt', 'r') as file:
        data = file.readlines()

    value = data[1:]
    values =  [float(i) for i in value]
    average_local = sum(values) / len(values)
    return average_local
    

average = get_average()
print(average)
            
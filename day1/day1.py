
def first(name = 'puzzle.txt'):
    with open(name, "r") as f:
        splitted = f.read().splitlines()
    
    numbers = [str(i) for i in range(1, 10)]

    acc: int = 0

    for line in splitted:
        lst_acc = []
        
        for num in numbers:
            try:
                lst_acc.append((num, line.index(num)))
            except:
                pass
            try:
                lst_acc.append((num, line.rindex(num)))
            except:
                pass
        
        lst_acc.sort(key= lambda x: x[1])
        print(lst_acc)
        print(int(lst_acc[0][0] + lst_acc[-1][0]))
        acc += int(lst_acc[0][0] + lst_acc[-1][0])

    print(acc)



def second():
    text_number = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    lines = []
    with open("puzzle.txt", "r") as f:
        data = f.read()

    for line in data.splitlines():#per ogni linea
        for number in text_number: #valuto il valore 
            if number in line:
                #controllare che il numero dopo non venga cambiato prima del precedente
                #quindi controllo che l'indice di quel valore venga prima e lo sostituisco
                line = line.replace(number, '{}{}{}'.format(number,text_number.index(number)+1,number))
        lines.append(line)
        	
    with open('puzzle_r.txt', 'w') as fp:
        for item in lines:
            fp.write(f"{item}\n")
    first_1('puzzle_r.txt')

if __name__ == "__main__":
    #first()
    second()
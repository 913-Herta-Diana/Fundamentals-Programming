
def bubble_sort(v,step1):
    k=0
    for i in range(len(v)):
        swap=False
        for j in range(0,len(v)-i-1):
            if v[j]>v[j+1]:
                aux=v[j]
                v[j]=v[j+1]
                v[j+1]=aux
                swap=True
                k+=1
                if (k == step1):
                    print(v)
                    k = 0
        if not swap:
                break
    if(k<step1):
        print(v)

def try_stooge(v,step):
    stooge_sort(v,0,generate_list.lenght,0,step)

def stooge_sort(v,left,right,k,step2):
    if left>=right:
        print("Invalid lenght of array")
        return
    k=step2
    if(v[left]>v[right]):
        aux = v[left]
        v[left] = v[right]
        v[right] = aux
        step2-=1
    if (step2 == 0):
        print(v)
        step2=k
    if(right-left+1>2):
        m=(right-left+1)//3
        stooge_sort(v,left,(right-m),k,step2)
        stooge_sort(v,left+m,right,k,step2)
        stooge_sort(v,left,(right-m),k,step2)

def menu():
    while True:
        print_menu()

        number = int(input('Enter n and generate n random numbers:'))

        generate_list(number)
        randomlist=generate_list.mylist

        option = int(input('Choose an option: '))

        try:
            assert 0<option<4
        except:
            print('The input does not satisfy the requirements.\nPlease input a valid value.')

        if option==1:
            step=int(input('Input the number of steps:'))
            bubble_sort(randomlist,step)
        elif option==2:
            step = int(input('Input the number of steps:'))
            try_stooge(randomlist,step)
        elif option==3:
            print('Exiting the menu')
            break
def print_menu():

    menu_options = {
        1: 'Option 1: Sort using Bubble Sort',
        2: 'Option 2: Sort using Stooge Sort',
        3: 'Exit'
    }
    for option in menu_options.keys():
        print(option,'.',menu_options[option])

def generate_list(n):
    import random
    generate_list.mylist = []
    initial = []
    for i in range(n):
        x = random.randint(0, 100)
        generate_list.mylist.append(x)
        initial.append(x)
    generate_list.lenght=len(generate_list.mylist)-1
    print(generate_list.mylist)


if __name__ == '__main__':
    menu()






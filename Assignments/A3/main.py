import time

def  bubble_sort(v,step1):
    k = 0
    start_time = time.time()
    for i in range(len(v)):
        swap=False
        for j in range(0,len(v)-i-1):
            if v[j]>v[j+1]:
                aux=v[j]
                v[j]=v[j+1]
                v[j+1]=aux
                swap = True
                k += 1
                if (k == step1):
                    k = 0
        if not swap:
                break
    end_time = time.time()
    execution_time = end_time - start_time
    print('For an array with', len(v), 'elements, the execution time is ', execution_time, '\n')

def try_stooge(v,step):
    stooge_sort(v,0,len(v)-1,0,step)
    
def stooge_sort(v,left,right,k,step2):
    if left>=right:
        return
    k = step2
    if (v[left] > v[right]):
        aux = v[left]
        v[left] = v[right]
        v[right] = aux
        step2 -= 1
    if (step2 == 0):
        step2 = k
    if (right - left + 1 > 2):
        m = (right - left + 1) // 3
        stooge_sort(v, left, (right - m), k, step2)
        stooge_sort(v, left + m, right, k, step2)
        stooge_sort(v, left, (right - m), k, step2)

def case_bubble(case,step3):
    if case == 1:
        worst_case(create_lists.list1)
        worst_case(create_lists.list2)
        worst_case(create_lists.list3)
        worst_case(create_lists.list4)
        worst_case(create_lists.list5)
        bubble_sort(create_lists.list1,step3)
        bubble_sort(create_lists.list2,step3)
        bubble_sort(create_lists.list3,step3)
        bubble_sort(create_lists.list4,step3)
        bubble_sort(create_lists.list5,step3)
    elif case == 2:
        bubble_sort(create_lists.list1,step3)
        bubble_sort(create_lists.list2,step3)
        bubble_sort(create_lists.list3,step3)
        bubble_sort(create_lists.list4,step3)
        bubble_sort(create_lists.list5,step3)
    elif case == 3:
        best_case(create_lists.list1)
        best_case(create_lists.list2)
        best_case(create_lists.list3)
        best_case(create_lists.list4)
        best_case(create_lists.list5)
        bubble_sort(create_lists.list1,step3)
        bubble_sort(create_lists.list2,step3)
        bubble_sort(create_lists.list3,step3)
        bubble_sort(create_lists.list4,step3)
        bubble_sort(create_lists.list5,step3)
def case_stooge(case,step3):

    if case == 1:
        best_case(create_lists.list1)
        best_case(create_lists.list2)
        best_case(create_lists.list3)
        best_case(create_lists.list4)
        best_case(create_lists.list5)

        start_time = time.time()
        try_stooge(create_lists.list1,step3)
        end_time=time.time()
        print('For an array with', len(create_lists.list1), 'elements, the execution time is ', end_time-start_time, '\n')

        start_time = time.time()
        try_stooge(create_lists.list2,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list2), 'elements, the execution time is ', end_time - start_time,'\n')

        start_time = time.time()
        try_stooge(create_lists.list3,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list3), 'elements, the execution time is ', end_time - start_time,'\n')

        start_time = time.time()
        try_stooge(create_lists.list4,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list4), 'elements, the execution time is ', end_time - start_time,'\n')

        start_time = time.time()
        try_stooge(create_lists.list5,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list5), 'elements, the execution time is ', end_time - start_time,'\n')

    elif case == 2:
        start_time = time.time()
        try_stooge(create_lists.list1,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list1), 'elements, the execution time is ', end_time - start_time,'\n')

        start_time = time.time()
        try_stooge(create_lists.list2,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list2), 'elements, the execution time is ', end_time - start_time,'\n')

        start_time = time.time()
        try_stooge(create_lists.list3,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list3), 'elements, the execution time is ', end_time - start_time,'\n')

        start_time = time.time()
        try_stooge(create_lists.list4,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list4), 'elements, the execution time is ', end_time - start_time,'\n')

        start_time = time.time()
        try_stooge(create_lists.list5,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list5), 'elements, the execution time is ', end_time - start_time,'\n')

    elif case == 3:
        worst_case(create_lists.list1)
        worst_case(create_lists.list2)
        worst_case(create_lists.list3)
        worst_case(create_lists.list4)
        worst_case(create_lists.list5)
        start_time = time.time()
        try_stooge(create_lists.list1,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list1), 'elements, the execution time is ', end_time - start_time,'\n')

        start_time = time.time()
        try_stooge(create_lists.list2,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list2), 'elements, the execution time is ', end_time - start_time,'\n')

        start_time = time.time()
        try_stooge(create_lists.list3,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list3), 'elements, the execution time is ', end_time - start_time,'\n')

        start_time = time.time()
        try_stooge(create_lists.list4,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list4), 'elements, the execution time is ', end_time - start_time,'\n')

        start_time = time.time()
        try_stooge(create_lists.list5,step3)
        end_time = time.time()
        print('For an array with', len(create_lists.list5), 'elements, the execution time is ', end_time - start_time,'\n')


def menu():
    while True:
        print_menu()
        option = int(input('Choose an option: '))
        try:
            assert 0 < option < 4
        except:
            print('The input does not satisfy the requirements.\nPlease input a valid value.')
        else:
            if option==3:
                print('Exiting the menu')
                break
            complexity_menu()
            case = int(input('Choose which case to consider: '))
            try:
                assert 0 < case < 4
            except:
                print('The input does not satisfy the requirements.\nPlease input a valid value.')
            else:
                if option==1:
                    create_lists()
                    step = int(input('Input the number of steps:'))
                    case_bubble(case,step)
                elif option==2:
                    create_lists()
                    step = int(input('Input the number of steps:'))
                    case_stooge(case,step)


def print_menu():

    menu_options = {
        1: 'Option 1: Sort using Bubble Sort',
        2: 'Option 2: Sort using Stooge Sort',
        3: 'Exit'
    }
    for option in menu_options.keys():
        print(option,'.',menu_options[option])

def complexity_menu():
    complexity_options={
        1: 'Option: Worst Case',
        2: 'Option: Average Case',
        3: 'Option: Best Case'
    }
    for option in complexity_options.keys():
        print(option,'.',complexity_options[option])

def create_lists():
    import random
    create_lists.list1=[]
    create_lists.list2=[]
    create_lists.list3=[]
    create_lists.list4=[]
    create_lists.list5=[]
    p=1
    for i in range(1,6):
        for j in range(100*p):
            x = random.randint(0, 100)
            if p==1:
                create_lists.list1.append(x)
            elif p==2:
                create_lists.list2.append(x)
            elif p==4:
                create_lists.list3.append(x)
            elif p==8:
                create_lists.list4.append(x)
            elif p==16:
                create_lists.list5.append(x)
        p*=2
    print(create_lists.list1,"\n")
    print(create_lists.list2, "\n")
    print(create_lists.list3, "\n")
    print(create_lists.list4, "\n")
    print(create_lists.list5, "\n")


def best_case(v):
    for i in range(len(v)):
        swap = False
        for j in range(0, len(v) - i - 1):
            if v[j] > v[j + 1]:
                aux = v[j]
                v[j] = v[j + 1]
                v[j + 1] = aux
                swap = True
        if not swap:
            break

def worst_case(v):
    for i in range(len(v)):
        swap = False
        for j in range(0, len(v) - i - 1):
            if v[j] < v[j + 1]:
                aux = v[j]
                v[j] = v[j + 1]
                v[j + 1] = aux
                swap = True
        if not swap:
            break



if __name__ == '__main__':
    menu()






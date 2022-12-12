'''1.A number of n coins are given, with values of a1, ..., an and a value s.
Display all payment modalities for the sum s.
If no payment modality exists print a message.
Implement both
1. Iterative
2. Recursive
methods

'''
vis = [] #to avoid going back to same element in
# backtracking if it is taken already as a solution
c = False #if there are solutions in backtracking
c2 = False #if there are solutions in iterative backtracking
sol = [] #for no repetition in backtracking

def valid(x,k,n,s,st,sol): #check if the element we want to add to the list is lower
    #than the sum for recursive
    if x <= s and k < n:
        sumc = sum(st)
        if sumc + x <= s:
            st2 = st.copy()  #doesnt repeat
            st2.append(x)
            st2.sort()
            if st2 in sol:
                return False  #doesnt repeat
            return True
    return False


def solution(s,st): #O(k)
    sumc = sum(st)
    if sumc == s:
        return True
    return False


def show():
    print(st) #O(1)


def back(coin_list, n, s, k): #O(k^n)
    for i in range(k,n):
        if vis[i] == 0:
            x = coin_list[i]
            if valid(x,k,n,s,st,sol):
                st.append(x)
                vis[i] = 1
                if solution(s,st):
                    show()
                    sumc = st.copy() #for no repetition
                    sol.append(sumc) #for no repetition
                    global c
                    c = True
                else:
                    back(coin_list, n, s, k + 1)
            vis[i] = 0
            if len(st) > 0:
                st.pop() #removes the item at the given index
                # and returns the removed item.
solutions = []

def is_consistent(cur_sol,s):
    if sum(cur_sol) <= s:
        return True
    return False

def is_solution(cur_sol,s):
    if sum(cur_sol) == s:
        return True
    return False

def bkt_iterative(n: int, values: list, s: int):
    k = 0
    cur_sol = [-1] * n
    while k > -1:
        if k == n:
            if is_solution(cur_sol, s):
                global solutions
                global c2
                c2=True
                if not solutions:
                    print("Solutions:")
                new_cur_sol = []
                for nr in cur_sol:
                    if nr != 0:
                        new_cur_sol.append(nr)
                if new_cur_sol not in solutions:
                    print(new_cur_sol)
                    solutions.append(new_cur_sol[:])
            k -= 1
            continue
        if cur_sol[k] == -1:
            cur_sol[k] = 0 #dont use it
        elif cur_sol[k] == 0:
            cur_sol[k] = values[k] #current element
            if not is_consistent(cur_sol, s):
                cur_sol[k] = -1
                k -= 1
                continue
        else: #checked all possibilities
            cur_sol[k] = -1
            k -= 1
            continue
        k+=1

if __name__ == "__main__":
    l = []
    n = int(input('The number of available coins is: '))
    for i in range(n):
        x = int(input("Coin value: "))
        l.append(x)
    s = int(input('The sum required for payment is:'))
    l.sort() #sorts the list ascending
    print('The available coins are:', l)
    print('Iterative: the sum,', s, 'can be paid as:')
    bkt_iterative(n,l,s)
    if c2 == False:
        print('not possible with available coins.')
    st = [] #solution for managing them
    vis = [0]*n
    print('Backtracking: the sum', s, 'can be paid as:')
    back(l, n, s, 0)
    if c == False:
        print('not possible with available coins.')
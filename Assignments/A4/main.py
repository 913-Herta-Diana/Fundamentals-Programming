# Given the set of positive integers S and the natural number k. display one of the subsets of S which sum to k.
#We divide the problem in two subproblems
#Rows will represent each element of the array
#Divide in subproblems: take the intermediate sums: last column=solution

def dynamic_check(arr,s):

    n=len(arr)

    matrix=([[False for i in range(s+1)]for i in range(n+1)])

    for i in range(n+1):
         matrix[i][0] = True

    for i in range(1, s + 1):
        matrix[0][i] = False

    for i in range(1,n+1):
        for j in range(1,s+1):
            if j<arr[i-1]:
                matrix[i][j]=matrix[i-1][j]
            else:
                matrix[i][j]=(matrix[i-1][j] or matrix[i-1][j-arr[i-1]])

    return matrix[n][s]
# dp[i][j] means the subset between 0...i that sum up to j
# The subsets store indices instead of values because the array can have duplicates.
def find_one_subset(arr,s):
    n = len(arr)
    matrix=([[set() for i in range(s+1)]for i in range(n+1)])

    for j in range(1,s+1):
        for i in range(n):
            if j-1>=0:
                matrix[i][j]=matrix[i-1][j]
            if(j-arr[i]>=0):
                prev_sol=matrix[i-1][j-arr[i]]
                if prev_sol is not None:
                    matrix[i][j]=prev_sol | set([i])
    output=matrix[n-1][s]
    return None if output is None else [arr[i] for i in output]




def naiveimplementation(arr, s):
    sets = [[]] #to go through and to store
    for i in arr:
        nextPart = []
        for j in sets:
            nextNum = j + [i] #add the number to the subset
            nextPart.append(nextNum) #add the subset to an array (list of subsets_
            if sum(nextNum) == s:
                return nextNum
        sets += nextPart
    return False

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k=int(input("Input the value of the sum: "))
    option=int(input("Choose 1 for the naive implementation or 2 for the dynamic one: "))
    if option==1:
        print(naiveimplementation(arr, k))
    else:
        #print(dynamic_check(arr,k))
        print(find_one_subset(arr, k))
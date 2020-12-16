#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

def diffPossible(A, B):
    dict = {}
    test = 0
    for i in range(len(A)):
        num1 = A[i] - B
        num2 = A[i] + B
        if (num1 in dict) or (num2 in dict):
            return 1
        if A[i] not in dict:
            dict[A[i]] = i
    return test


a = [1,5,3]
k = 2
print(diffPossible(a, k))
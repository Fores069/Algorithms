substring = "lower"
p = [0] * len(substring)
j = 0
i = 1

while i < len(substring):
    if substring[j] == substring[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

string = "lomewlowe rowellower"

m = len(substring)
n = len(string)

i = j = 0
while i < n:
    if string[i] == substring[j]:
        i += 1
        j += 1
        if j == m:
            print(True)
            break
    else:
        if j > 0:
            j = p[j - 1]
        else:
            i += 1
            if i == n:
                print(False)
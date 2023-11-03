sample = "данные"


sample_length = len(sample)
bias_dct = {}     

for i in range(sample_length-2, -1, -1):
    if not bias_dct.get(sample[i]):
        bias_dct[sample[i]] = sample_length-i-1

if not bias_dct.get(sample[-1]):
    bias_dct[sample[sample_length-1]] = sample_length

bias_dct['*'] = sample_length


string = "метеоданные"
string_length = len(string)


def get_off(j):
    if j == sample_length-1:
        return bias_dct[string[i]] if bias_dct.get(string[i], False) else bias_dct['*']
    else:
        return bias_dct[sample[j]]


if string_length >= sample_length:
    i = sample_length-1    

    while i < string_length:
        k = 0
        j = 0
        flBreak = False
        for j in range(sample_length-1, -1, -1):
            if string[i-k] != sample[j]:
                i += get_off(j)
                flBreak = True  
                break

            k += 1        

        if not flBreak:
            print(f"образ найден по индексу {i-k+1}")
            break
    else:
        print("образ не найден")
else:
    print("образ не найден")
#Escape Pods
def solution(entry, exit, matrix):
    overall = 0
    nuk = len(matrix[:])
    interm_entry = [0]* nuk
    for i in entry:
        k = matrix[i]
        for j in range(len(k)):
            if j in exit:
                overall += k[j]
                continue
            interm_entry[j] += k[j]
    for i in range(nuk):
        if i not in entry:
            k = matrix[i]
            for j in range(nuk):
                if j in entry:
                    continue
                if interm_entry[i] > 0:
                    interm_entry[i] -=k[j]
                    if interm_entry[i] <0:
                        k[j] += interm_entry[i]
                    if j in exit:
                        overall += k[j]
                        continue
                    interm_entry[j] += k[j]
    return overall

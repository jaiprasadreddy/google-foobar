
def set_let(l, count_dict):
    def value(e1):
        k1 = e1.split('.')
        if len(k1) > l:
            count_dict[int(k1[l])] = count_dict.get(int(k1[l]),0)+1
            return int(k1[l])
        else:
            count_dict[-1] = e1
            return -1
    return value

def sort_index(l2, index= 0):
    count_dict = {}
    k1 = set_let(l=index, count_dict=count_dict)
    s1 = sorted(l2, key=k1)
    c1 = sorted(count_dict.items())
    return s1,c1

# this can be a reccursive function will update this.
def solution(l):
    final_list = []
    f1, c1 = sort_index(l,index=0)
    idx = 0
    for i,j in c1:
        if j <= 1:
            final_list.extend([f1[idx]])
            idx += j
        else:
            sublist1 = f1[idx:idx+j]
            idx +=j
            f2, c2 = sort_index(sublist1,index=1)
            idx2 = 0
            print(c2)
            for i1, j1 in c2:
                if i1 == -1:
                    final_list.extend(j1)
                    idx2 += 1
                    continue
                if j1 <= 1:
                    final_list.extend([f2[idx2]])
                    idx2 += j1
                else:
                    sublist2 = f2[idx2:idx2 + j1]
                    f3, c3 = sort_index(sublist2, index=2)
                    final_list.extend(f3)
                    idx2 = idx2 + j1
    return final_list


solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])

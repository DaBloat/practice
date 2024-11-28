# Given the list of Items use k as the number of steps
# Get the kth position and add it to the permutation, delete in the original
# continue until the original list is null
# if len(origList) < k, the remaining data is added to the permutation 1 by 1

def josephus1(items, k):
    # True but Rejected
    orig = items
    perm = []
    attach = []
    while len(orig) > 0:
        for i in range(len(orig)):
            if (i+1) % k == 0:
                perm.append(orig[i])
            else:
                attach.append(orig[i])

        if len(orig) % k != 0:
            last = attach.pop()
            attach.insert(0, last)

        orig = attach
        attach = []

        if len(orig) == 1:
            perm.append(orig.pop())
    return perm


def josephus(items, k):
    perm = []
    cnt = 1
    while len(items) > 0:
        if cnt % k == 0:
            perm.append(items.pop(0))
            cnt += 1
        else:
            items.append(items.pop(0))
            cnt += 1
    return perm



print(josephus([1,2,3,4,5,6,7,8,9,10],1))
# print(josephus([],3))


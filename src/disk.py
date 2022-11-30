st = "Software Engineering Career Program"

strArr = st.split()

strArr = [sorted(i, reverse=True) for i in strArr]


def mergeList(list):
    revList = []
    for i in list:
        i.append(" ")
        revList += i
    return revList[0 : len(revList) - 1]


print(mergeList(sorted(strArr)))
